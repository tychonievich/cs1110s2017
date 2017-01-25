#!/usr/bin/env python3



class Table(object):
	def __str__(self):
		return str(self.__class__).split("'")[1].split('.')[-1].lower()
	@staticmethod
	def escape(value):
		if value is None: return 'null'
		return "'{}'".format(str(value).replace("'", "''"))
	@classmethod
	def columns(cls):
		'''returns a generator with all column names'''
		return (x for x in dir(cls) if x not in dir(Table))
	@classmethod
	def create(cls):
		'''exeute a CREATE TABLE statement'''
		cls.db.execute('CREATE TABLE IF NOT EXISTS ' + str(cls()) + ' ( '
			+ ', '.join(x + ' ' + cls.__getattribute__(cls, x) for x in dir(cls) if x not in dir(Table))
			+ ' );')
	@classmethod
	def select(cls, tail=''):
		'''returns a generator with the results of the query'''
		columns = list(cls.columns())
		stmt = 'SELECT ' + ', '.join(columns) + ' FROM ' + str(cls())+ ' ' + tail + ';'
		cur = cls.db.execute(stmt)
		return (dict((columns[i], row[i]) for i in range(len(columns))) for row in cur.fetchall())
	@classmethod
	def sellist(cls, tail=''):
		return list(cls.select(tail))
	@classmethod
	def selone(cls, tail=''):
		columns = list(cls.columns())
		stmt = 'SELECT ' + ', '.join(columns) + ' FROM ' + str(cls())+ ' ' + tail + ' LIMIT 1;'
		cur = cls.db.execute(stmt)
		try:
			row = cur.fetchone()
			return dict((columns[i], row[i]) for i in range(len(columns)))
		except:
			return None
	@classmethod
	def execute(cls, template, args):
		return cls.db.execute(template.format(*(Table.escape(s) for s in args)))
	@classmethod
	def update(cls, kv, where=[]):
		if not where:
			for c in cls.columns():
				kind = cls.__getattribute__(cls, c).upper()
				if c in kv and ('PRIMARY' in kind or 'UNIQUE' in kind):
					where.append(c)
		cls.db.execute('UPDATE ' + str(cls()) + ' SET '
			+ ', '.join("{} = {}".format(k, Table.escape(kv[k])) for k in kv if k not in where)
			+ ' WHERE '
			+ ' AND '.join("{} = {}".format(k, Table.escape(kv[k])) for k in where)
			+ ';'
		)
		cls.db.commit()
	@classmethod
	def insert(cls, kv):
		stmt = ('INSERT OR IGNORE INTO ' + str(cls()) + ' ( '
			+ ', '.join("{}".format(k) for k in kv if k)
			+ ' ) VALUES ( '
			+ ', '.join("{}".format(Table.escape(kv[k])) for k in kv if k)
			+ ' );'
		)
		cls.db.execute(stmt)
		cls.db.commit()
	@classmethod
	def delete(cls, where):
		cls.db.execute('DELETE FROM '+str(cls())+' WHERE '
			+ ' AND '.join("{} = {}".format(k, Table.escape(where[k])) for k in where)
			+ ';')
		cls.db.commit()
		
def where(kv):
	return ' WHERE ' + ' AND '.join("{} = {}".format(k, Table.escape(kv[k])) for k in kv);

class Person(Table):
	compid = 'PRIMARY KEY'
	name = 'TEXT'
	image = 'TEXT' 
	role = 'TEXT' 
	section = 'TEXT'
	help_time = 'INTEGER'
	last_helped = 'INTEGER'
class Queue(Table):
	compid = 'UNIQUE REFERENCES person(compid)'
	location = 'TEXT'
	purpose = 'TEXT'
	entered = 'INTEGER'
	helped_at = 'INTEGER'
	helped_by = 'REFERENCES person(compid)'
	priority = 'INTEGER'
class Log(Table):
	compid = 'TEXT REFERENCES person(compid)'
	purpose = 'TEXT'
	entered = 'INTEGER'
	helped_at = 'INTEGER'
	helped_by = 'REFERENCES person(compid)'
	finished_at = 'INTEGER'
	finished_notes = 'TEXT'
	




import sqlite3
from time import time
now = int(time())
Table.db = sqlite3.connect('queue.db')

# print(Table.db.execute('SELECT * FROM sqlite_master;').fetchall())

def setup():
	Person.create()
	Queue.create()
	Log.create()
	Person.insert({'compid':'lat7h', 'name':'Tychonievich, Luther', 'role':'Staff'})
	Person.insert({'compid':'mst3k', 'name':'Theater, Mystery Science', 'role':'Student', 'help_time':0, 'last_helped':0, 'section':'1111'})
	with open('roster.sql') as f:
		for line in f:
			Table.db.execute(line)
	Table.db.commit()	

_person = {}
def person(compid):
	'''return a person object'''
	global _person
	if compid not in _person:
		_person[compid] = Person.selone(where({'compid':compid}))
	return _person[compid]

_queue = None
def queue():
	'''return the entire queue'''
	global _queue
	if _queue is None:
		_queue = Queue.sellist('ORDER BY priority ASC')
	return _queue

def queue_position(compid):
	'''return the number of people in front of compid, or None if not on queue'''
	priority = Queue.selone(where({'compid':compid}))
	if priority is None: return None
	waiting = int(priority['helped_by'] is None)
	priority = priority['priority']
	return Table.db.execute('SELECT count(*) FROM queue WHERE priority < '+str(priority) + " AND typeof(helped_by) = 'null';").fetchone()[0] + waiting

def queue_size():
	return Table.db.execute("SELECT count(*) FROM queue WHERE typeof(helped_by) = 'null';").fetchone()[0]

def enqueue(compid, location, purpose):
	'''Place this person on the queue (if not already there)'''
	Queue.insert({
		'compid':compid,
		'location':location,
		'purpose':purpose,
		'entered':now,
		# ignore the time on the queue; the question is (1) how long since last help_specific and (2) how much total TA time have you consumed so far
		'priority':person(compid)['last_helped'] + 10*person(compid)['help_time'],
	})
	_queue = None

def help_specific(student, ta):
	'''Claims a student for a TA'''
	Queue.update({
		'compid':student,
		'helped_by':ta,
		'helped_at':now,
	})
	_queue = None
	if student in _person: del _person[student]
	return Queue.selone(where({'compid':student}))

def help_first(ta):
	'''Claims the student at the head of the queue and returns that request'''
	claimant = Queue.selone('ORDER BY priority ASC')
	if claimant is None: return None
	help_specific(claimant['compid'], ta)
	claimant['helped_by'] = ta
	claimant['helped_at'] = now
	return claimant

def unhelp_all(ta):
	'''returns any students being helped by this TA to the queue unhelped'''
	rows = Queue.sellist(where({'helped_by':ta}))
	for row in rows:
		Queue.update({'compid':row['compid'], 'helped_by':None, 'helped_at':None})
		for e in list(row.keys()):
			if e not in Log.columns():
				del row[e]
		row['finished_at'] = now
		row['finished_notes'] = 'not helped'
		Log.insert(row)

def resolve(student, ta=None, message='request retracted'):
	'''removes a queued request from the queue'''
	row = Queue.selone(where({'compid':student}))
	if row is None or ta is None and row['helped_by'] is not None:
		return False # illegal request by student to stop clocking ongoing help_specific 
	Queue.delete({'compid':student})
	for e in list(row.keys()):
		if e not in Log.columns():
			del row[e]
	row['finished_at'] = now
	row['finished_notes'] = message
	Log.insert(row)
	if row['helped_at'] is not None:
		Person.update({
			'compid':student, 
			'last_helped':now, 
			'help_time':person(student)['help_time'] + now - row['helped_at'],
		})
		del _person[student]
	return True

def change_purpose(student, purpose):
	'''updates the purpose of an in-queue help_specific request'''
	Queue.update({
		'compid':student,
		'purpose':purpose,
	})



if __name__ == '__main__':
	setup()
