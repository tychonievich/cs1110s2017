#!/usr/bin/env python3

from queue import *
import os, datetime, cgi, html
import cgitb
cgitb.enable()

def pretty_time(secs):
	if secs < 60: return str(secs)+" seconds"
	if secs < 3600: return '{}:{:02}'.format(secs//60, secs%60)
	else: return '{} hours'.fomat(secs//3600)

# step one: authenticate
print('Content-Type: text/html')
print('')
form = cgi.FieldStorage()
user = os.environ["REMOTE_USER"]

if user == 'lat7h' and 'asuser' in form:
	user = form['asuser'].value

me = person(user)
if me is None:
	print('Sorry, user {} is not on our roles'.format(repr(user)))
	exit()
else:
	print('<p>Logged in as {} ({}), a {}</p>'.format(me['name'], user, me['role']))


if me['role'] == 'Student':
	me['pos'] = queue_position(user)
	me['entry'] = Queue.selone(where({'compid':user}))
else:
	me['helping'] = Queue.selone(where({'helped_by':user}))

print('''<!DOCTYPE html>
<html><head>
	<meta charset="UTF-8">
	<style>
	input { font-size: 100%; }
	input[type=submit] { min-width:3em; min-height:3em; margin:1ex; }
	.warning { display: inline-block; background-color:#ff7; padding:1ex; }
	table { border-collapse: collapse; border: 1px solid black; }
	th, td { padding: 0ex 1ex; }
	thead { border-bottom: thin solid black; }
	tbody th { padding: 1ex; text-align: left; }
	</style>
	<title>CS 1110 Office Hour Queue</title>
</head><body>
''')


# step two: handle requests

if 'enter' in form:
	# e.g. enter=stuck with loops&where=A3
	if 'where' not in form:
		print('<p class="warning">Failed to state where you are located</p>')
	elif me['role'] == 'Student':
		purpose = form['enter'].value
		location = form['where'].value
		if me['pos'] is None:
			enqueue(user, location, purpose)
			me['pos'] = queue_position(user)
			me['entry'] = Queue.selone(where({'compid':user}))
		else:
			Queue.update({
				'compid':user,
				'purpose':purpose,
				'location':location,
			})
			me['entry'].update({
				'purpose':purpose,
				'location':location,
			})
	else:
		print('<p class="warning">TAs are not allowed to enter the queue</p>')
if 'help' in form:
	# e.g. help=mst3k
	if me['role'] == 'Student':
		print('<p class="warning">Students are not allowed to mark people as helped</p>')
	elif me['helping'] is not None:
		print('<p class="warning">You are already helping another student</p>')
	else:
		whom = form['help'].value
		if whom == 'first':
			me['helping'] = help_first(user)
			if me['helping'] is None:
				print('<p class="warning">The queue is empty</p>')
		else:
			me['helping'] = help_specific(whom, user)
			if me['helping'] is None:
				print('<p class="warning">That student is not on the queue</p>')
if 'resolve' in form:
	# e.g. resolve=mst3k&msg=not in stacks
	if me['role'] == 'Student':
		if not resolve(user):
			print('<p class="warning">You can\'t resolve your request because you are not on the queue</p>')
		else:
			me['pos'] = None
			me['entry'] = None
	else:
		if not resolve(form['resolve'].value, user, form['msg'].value):
			print('<p class="warning">You can\'t resolve a student who has no pending request</p>')
		else:
			me['helping'] = None

			
	


# step three: show menu

if 'tud' in me['role']:
	pos = queue_position(user)
	if pos is None:
		print('<p>You are not currently on the queue (current queue size: {})</p>'.format(queue_size()))
		print('''
		<form action="" method="POST">
		<p>What help do you need?</p>
		<textarea name="enter"></textarea>
		<p>Each seat in Stacks should have <a href="../StacksStickers.png" target="_blank">a seat id</a> (a letter-number pair, like A6 or M3). Where are you? <input type="text" name="where"/>
		<input type="submit" value="Request Help"/>
		</form>
		''')
	else:
		print('<p>You are at queue position {}</p>'.format(pos))
		print('''
		<form action="" method="POST">
		<p>You may <input type="submit" name="resolve" value="Retract your request"/></p>
		</form>

		<form action="" method="POST">
		<p>You may change your purpose text</p>
		<textarea name="enter">{}</textarea>
		<p>and/or your location <input type="text" name="where" value="{}"/>
		<input type="submit" value="Update request"/>
		</form>
		'''.format(html.escape(me['entry']['purpose']), html.escape(me['entry']['location'])))
else:
	if 'display' in form:
		print('''<table><thead><tr><th>ID</th><th>Location</th><th>Wait time</th><th>Purpose</th><tr></thead>
		<tbody>''')
		for entry in queue():
			print('<tr><td><form action="" method="POST"><input type="submit" name="help" value="{}"/></form></td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(
				entry['compid'],
				html.escape(entry['location']),
				'being helped' if entry['helped_at'] is not None else pretty_time(now - entry['entered']),
				html.escape(entry['purpose']),
			))
		print('<tbody></table>')
	else:
		print('<p>Current queue size: {}</p>'.format(queue_size()))
	if me['helping'] is None:
		print('''
		<form action="" method="POST">
			<input type="hidden" name="help" value="first"/>
			<input type="submit" value="Help first student on queue"/>
		</form>
		
		<form action="" method="POST">
			<input type="submit" name="display" value="Show full queue"/>
		</form>
		''')
	else:
		stud = Person.selone(where({'compid':me['helping']['compid']}))
		stud.update(me['helping'])
		print('''<p>Currently helping student:</p>
		<table><tbody>
		<tr><th>Location</th><td>{}</td></tr>
		<tr><th>Name</th><td>{}</td></tr>
		<tr><th>Image</th><td><img src="{}"/></td></tr>
		<tr><th>Purpose</th><td>{}</td></tr>
		</tbody><table>
		'''.format(
			html.escape(stud['location']),
			html.escape(stud['name']),
			stud['image'],
			html.escape(stud['purpose']),
		))
		print('''
		<p>Resolve as
		<form action="" method="POST">
		<input type="hidden" name="resolve" value="{0}"/>
		<input type="submit" name="msg" value="Bad location"/>
		<input type="submit" name="msg" value="Wanted answer, not help"/>
		<input type="submit" name="msg" value="Off-topic"/>
		<input type="submit" name="msg" value="Didn't read"/>
		<input type="submit" name="msg" value="Debugging help"/>
		<input type="submit" name="msg" value="Design help"/>
		<input type="submit" name="msg" value="Conceptual help"/>
		<input type="submit" name="msg" value="Wanted reassurance"/>
		</form>
		</p><p>Or enter your own comments:
		<form action="" method="POST">
		<input type="hidden" name="resolve" value="{0}"/>
		<input type="text" name="msg"/>
		<input type="submit" value="Other"/>
		</form></p>
		'''.format(stud['compid']))

print('</body></html>')