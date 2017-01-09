import datetime
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

with open('cal-shared.yaml') as stream:
    data = load(stream, Loader=Loader)
with open('cal-1110-001.yaml') as stream:
    tmp = load(stream, Loader=Loader)
    luther = tmp['1110-001']
    lkey = tmp.get('key', ['topic'])
with open('cal-1110-002.yaml') as stream:
    tmp = load(stream, Loader=Loader)
    upsorn = tmp['1110-002']
    ukey = tmp.get('key', ['topic'])
with open('cal-1111.yaml') as stream:
    tmp = load(stream, Loader=Loader)
    craig = tmp['1111']
    ckey = tmp.get('key', ['topic'])

day = datetime.timedelta(days=1)

now = data['Special Dates']['Courses begin']
end = data['Special Dates']['Courses end']
lab = data['1110-lab']

print('''---
title: Schedule
...


<style>
.calender { border-collapse: collapse; }
.calender td { padding:0.5ex; }
.day { width:25%; border:thin solid black; vertical-align:top; }
.date { color:#777; font-size:80%; float:right; padding-left:1ex; margin-top:-0.8ex; }
.Monday { }
.Wednesday { }
.Thursday { }
.Thursday.day { border:none; }
.Friday { }
.noclass { background-color: #eee; color:#777; border:none; }
.exam, .special { background-color: #fda; }
span.special { white-space:pre; }
td span.special { display:block; margin:0ex -0.5ex; padding: 0ex 0.5ex;}
.agenda th+td { padding-left:1em; }
tr.lab { background-color: #fff7f0; }
.button { padding:1ex; margin:1ex; border-radius:0.5ex; background-color:#fda; display:inline-block;}
.button.visited { background-color:#eee; color:#777; }
</style>
<script>
function rehide(e) {
	var hash=window.location.hash;
	if (e) hash = e;
	if (typeof(hash) != "string") return;
	console.log("hash = " + hash);
	var elems = ['cal001', 'cal002', 'cal1111', 'age001', 'age002', 'age1111'];
	for(var i in elems) {
		var id = elems[i];
		if (hash == id || hash == '#'+id)
			document.getElementById(id).setAttribute('style', '');
		else
			document.getElementById(id).setAttribute('style', 'display:none;');
		if (hash == id || hash == '#'+id)
			document.getElementById('a'+id).setAttribute('class', 'button visited');
		else
			document.getElementById('a'+id).setAttribute('class', 'button');
		
	}
	return true;
}
</script>

<a id="acal001" class="button" href="#cal001" onclick="rehide('cal001')">1110-001 Calender</a>
<a id="aage001" class="button" href="#age001" onclick="rehide('age001')">1110-001 Agenda</a>
<a id="acal002" class="button" href="#cal002" onclick="rehide('cal002')">1110-002 Calender</a>
<a id="aage002" class="button" href="#age002" onclick="rehide('age002')">1110-002 Agenda</a>
<a id="acal1111" class="button" href="#cal1111" onclick="rehide('cal1111')">1111 Calender</a>
<a id="aage1111" class="button" href="#age1111" onclick="rehide('age1111')">1111 Agenda</a>

<hr/>

''')

cal001 = '''<table id="cal001" class="calender">
<thead><tr><th>Monday</th><th>Wednesday</th><th>Thursday</th><th>Friday</th></tr></thead>
<tbody><tr><td/>
'''
age001 = '''<table id="age001" class="agenda">
<thead><tr><th>Date</th><th>'''+'</th><th>'.join(s.title() for s in lkey)+'''</th></tr></thead>
<tbody>'''


cal002 = '''<table id="cal002" class="calender">
<thead><tr><th>Monday</th><th>Wednesday</th><th>Thursday</th><th>Friday</th></tr></thead>
<tbody><tr><td/>
'''
age002 = '''<table id="age002" class="agenda">
<thead><tr><th>Date</th><th>'''+'</th><th>'.join(s.title() for s in ukey)+'''</th></tr></thead>
<tbody>'''

cal1111 = '''<table id="cal1111" class="calender">
<thead><tr><th>Monday</th><th>Wednesday</th></tr></thead>
<tbody><tr><td/>
'''
age1111 = '''<table id="age1111" class="agenda">
<thead><tr><th>Date</th><th>'''+'</th><th>'.join(s.title() for s in ckey)+'''</th></tr></thead>
<tbody>'''

classes = {}
content = {}
def record(date, kind):
    global classes, content
    if kind.endswith('eadline'): 
        content.setdefault(date, []).append('<span class="special">'+kind+'</span>')
    elif kind.endswith('ecess') or kind.endswith('reak') or 'eading' in kind:
        classes.setdefault(date, []).append('noclass')
        content.setdefault(date, []).append('<span class="reason">'+kind+'</span>')
    elif 'xam' in kind:
        classes.setdefault(date, []).append('exam')

for d in data['Special Dates']:
    date = data['Special Dates'][d]
    if not isinstance(date, datetime.date):
        date2 = date['start']
        while date2 <= date['end']:
            record(date2, d)
            date2 += day
    else:
        record(date, d)

def mwf(date, index, ilab, section, key, friday=True):
    special = '<br/>'+'<br/>'.join(content.get(date, [])) if date not in classes else ''
    caldate = '<td class="day {2} {3}" id="{0}"><span class="date">{1}</span>'.format(
        date, 
        date.strftime('%d ').strip('0')+ date.strftime('%B')[:3], 
        date.strftime('%A'),
        ' '.join(classes.get(date, []))+(' lab' if date.weekday() == 3 else ''),
    )
    agedate = '<tr id="{0}" class="{2}"><th>{1} {3}</th><td>'.format(
        date, 
        date.strftime('%d ').strip('0')+ date.strftime('%B')[:3], 
        ' '.join(classes.get(date, []))+(' lab' if date.weekday() == 3 else ''),
        special
    )
    cal = ''
    age = ''
    if date.weekday() in ([0,2,4] if friday else [0,2]):
        if 'noclass' in classes.get(date, []):
            text = '\n'.join(content.get(date, []))
        else:
            if index < len(section) and section[index] is not None: text = section[index]
            else: text = ''
            index += 1
        if type(text) is not dict: text = {key[0]:text}
        cal = caldate + '<br/>'.join(text[k] for k in key if k in text) + special + '</td>\n'
        age = agedate + '</td><td>'.join(text.get(k,'') for k in key)
    elif date.weekday() == 3 and friday:
        if 'noclass' in classes.get(date, []):
            text = '\n'.join(content.get(date, []))
        else:
            if ilab < len(lab) and lab[ilab] is not None: text = lab[ilab]
            else: text = ''
            ilab += 1
        if type(text) is not dict: text = {key[0]:text}
        cal = caldate + '<br/>'.join(text[k] for k in key if k in text) + special + '</td>\n'
        age = agedate + '</td><td>'.join(text.get(k,'') for k in key)
    elif date.weekday() == 6:
        cal = '</tr><tr>\n'
    return cal, age, index, ilab



i1110 = 0
i1111 = 0
ilab = 0
while now < end:
	cx, ax, i1111, _ = mwf(now, i1111, ilab, craig, ckey, friday=False)
	c2, a2, _, _ = mwf(now, i1110, ilab, upsorn, ukey)
	c1, a1, i1110, ilab = mwf(now, i1110, ilab, luther, lkey)
	cal001 += c1
	age001 += a1
	cal002 += c2
	age002 += a2
	cal1111 += cx
	age1111 += ax
	now += day

cal001 += '</tr></tbody></table>'
age001 += '</tbody></table>'
cal002 += '</tr></tbody></table>'
age002 += '</tbody></table>'
cal1111 += '</tr></tbody></table>'
age1111 += '</tbody></table>'

print(cal001)
print(age001)
print(cal002)
print(age002)
print(cal1111)
print(age1111)

print('<script>rehide()</script>')
print('''
Per <a href="http://www.virginia.edu/registrar/exams.html#1172">the registrar</a>, all sections of 1110 and 1111 will have their final exam at 7--10 pm on Thursday, 11 May 2017.
Conflicts with that time will be resolved the following day (Friday 12 May).
No permission to take the exam earlier than 11 May or from off of UVa grounds will be granted.
''')
