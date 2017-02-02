#!/usr/bin/env python3

from queue import *
import os, datetime, cgi, html
import cgitb
cgitb.enable()

import sys
import sys; sys.stdout = open(1, 'w', encoding='utf-8', closefd=False)

def pretty_time(secs):
    from datetime import datetime
    if secs > 1000000000: # probably a date, not a time
        return datetime.fromtimestamp(secs).strftime('%d %b %H:%M')
    if secs < 60: return str(secs)+" seconds"
    if secs < 3600: return '{}:{:02}'.format(secs//60, secs%60)
    else: return '{}:{:02}:{:02}'.format(secs//3600, (secs//60)%60, secs%60)


# step one: authenticate
print('Content-Type: text/html; charset=UTF-8')
print('')
form = cgi.FieldStorage()
user = os.environ.get("REMOTE_USER", 'lat7h')

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
    body, table, th, td, input, select, option { font-size:100%; }
    textarea { width: 100%; }
    input[type=submit] { min-width:3em; min-height:3em; margin:1ex; }
    input[type=checkbox] { width:2em; height:2em; border: thin solid red; }
    .warning { display: inline-block; background-color:#ff7; padding:1ex; }
    table { border-collapse: collapse; border: 1px solid black; }
    th, td { padding: 0ex 1ex; }
    thead { border-bottom: thin solid black; }
    tbody th { padding: 1ex; text-align: left; }
    </style>
    <title>CS 1110 Office Hour Queue</title>
</head><body>
<p>TA Queue hours are 3&ndash;9pm Sunday through Thursday on days when class is in session.  Requests here will not be handled outside of those times.</p>
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
elif 'where' in form:
    print('<p class="warning">Failed to state what you need help with</p>')

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
        if not resolve(form['resolve'].value, user, '\n'.join(form.getlist('msg'))):
            print('<p class="warning">You can\'t resolve a student who has no pending request</p>')
        else:
            me['helping'] = None

if 'unhelp' in form:
    if me['role'] == 'Student':
        print('<p class="warning">Students are not allowed to mark people as unhelped</p>')
    else:
        unhelp_all(user)
        me['helping'] = None
    


# step three: show menu

refresh = '<form action="" method="POST"><input type="submit" value="Refresh queue status"/></form>'

if 'tud' in me['role']:
    pos = queue_position(user)
    if pos is None:
        print('<p>You are not currently on the queue (current queue size: {})</p>{}'.format(queue_size(), refresh))
        print('''
        <form action="" method="POST">
        <p>What help do you need?  If working on an assignment, start with the name of the assignment, like <code>c2f.py - always thinks the temperature is 0.0</code></p>
        <textarea name="enter"></textarea>
        <p>Each seat in Stacks should have <a href="../StacksStickers.png" target="_blank">a seat id</a> (a letter-number pair, like A6 or M3). Where are you? <br/><input type="text" name="where"/>
        <input type="submit" value="Request Help"/>
        </form>
        ''')
        #<p>What are you working on? <select name="task">
        #<option value="understanding concepts">understanding concepts</option>
        #</select></p>
        
        
    else:
        print('<p>You are at queue position {}</p>{}'.format(pos, refresh))
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
    if 'mylog' in form:
        print("""
        <hr/>
        <p>Log of help you've been given:</p>
        <table><thead><tr><th>Date</th><th>Duration</th><th>Busy Time?</th><th>Helper</th><th>Purpose</th></tr></thead>
        <tbody>""")
        for row in student_log(user):
            if row['finished_at'] is None or row['helped_at'] is None: continue
            print('<tr>',('<td>{}</td>'*5).format(
                pretty_time(row['finished_at']),
                pretty_time(row['finished_at'] - row['helped_at']),
                'Yes' if row['charged'] != 0 else 'No',
                row['helped_by'],
                row['purpose'],
            ),'</tr>')
        print('''</tbody></table>''')
    else:
        print('''<hr/><form action="" method="POST"><input type="submit" name="mylog" value="Show your help history"/></form>''')
    print('''
    <hr/>
    <p><b>How do we decide who to help first?</b></p>
    <p>
        Our goal is to provide fair access of help to all students,
        with an incentive to seek help during quiet periods and to have well-thought-out questions when you ask for help.
        To achieve this, we track two things:
        when you last got help, and how much TA time you've used during busy times.
        We then compute <code>time_last_helped + (busy_ta_time_used * 10)</code>;
        the person with the earliest such value who is asking for help is at the head of the queue.
    </p>
    <p>
        When the queue is not very full (≤ 5 people waiting), feel free to ask open-ended questions.
        When the queue is full (≥ 6 people waiting), try to keep your questions short and on topic.
        In all cases, put yourself on the queue when you have a question, not to "get in line":
        by tracking time of last help, you are effectively always in line.
    </p>
    <p>
        This order is a default only; TAs are empowered to handle requests in any order
        if they have reason to believe they can more perform their jobs that way.
    </p>
    ''')
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
        print('<p>Current queue size: {}</p>{}'.format(queue_size(), refresh))
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
        print('''
        <img src="//stardock.cs.virginia.edu/cs1110/StacksStickers.png" style="float:right"/>
        <p>Currently helping student:</p>
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
        <form action="" method="POST">
        <form action="" method="POST">
        <input type="hidden" name="unhelp" value="{0}"/>
        <input type="submit" value="Return to queue unhelped"/>
        </form>
        <p>Resolve as
        <form action="" method="POST">
        <input type="hidden" name="resolve" value="{0}"/>
        '''.format(stud['compid']), 
        '<br/>\n'.join('<label><input type="checkbox" name="msg" value="{0}"/> {0}</label>'.format(s) for s in [
            "Conceptual help",
            "Debugging help",
            "Design help",
            "Didn't read assignment",
            "Not here",
            "Off-topic",
            "Wanted answer, not learning",
            "Wanted reassurance",
        ]), '''
        <br/>Other: <input type="text" name="msg"/><br/>
        <input type="submit" value="Finish with student"/>
        </form>
        ''')
    if 'mylog' in form:
        print("""
        <hr/>
        <p>Log of help you've given:</p>
        <table><thead><tr><th>ID</th><th>Date</th><th>Duration</th><th>Seat</th><th>Purpose</th><th>Report</th></tr></thead>
        <tbody>""")
        for row in ta_log(user):
            if row['finished_at'] is None or row['helped_at'] is None: continue
            print('<tr>',('<td>{}</td>'*6).format(
                row['compid'],
                pretty_time(row['finished_at']),
                pretty_time(row['finished_at'] - row['helped_at']),
                row['location'],
                row['purpose'],
                row['finished_notes'],
            ),'</tr>')
        print('''</tbody></table>''')
    else:
        print('''<hr/><form action="" method="POST"><input type="submit" name="mylog" value="Show your help history"/></form>''')

print('</body></html>')
