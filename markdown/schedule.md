---
title: Schedule
...

<style>
.calender { border-collapse: collapse; }
.calender td { padding:0.5ex; }
/* .calender tbody tr { height:6em; } */
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
</style>
<script>
function rehide() {
	var hash=window.location.hash;
	if (typeof(hash) != "string") return;
	console.log("hash = " + hash);
	var elems = ['cal001', 'cal002', 'cal1111', 'age001', 'age002', 'age1111'];
	for(var i in elems) {
		var id = elems[i];
		if (hash == id || hash == '#'+id)
			document.getElementById(id).setAttribute('style', '');
		else
			document.getElementById(id).setAttribute('style', 'display:none;');
	}
}
</script>

<table id="cal001" class="calender">
<thead><tr><th>Monday</th><th>Wednesday</th><th>Thursday</th><th>Friday</th></tr></thead>
<tbody><tr><td/>
<td class="day Wednesday " id="2017-01-18"><span class="date">18 Jan</span>welcome<br/></td>
<td class="day Thursday  lab" id="2017-01-19"><span class="date">19 Jan</span>installing Python and PyCharm<br/></td>
<td class="day Friday " id="2017-01-20"><span class="date">20 Jan</span>from requirements to software<br/></td>
</tr><tr>
<td class="day Monday " id="2017-01-23"><span class="date">23 Jan</span>ambiguity<br/></td>
<td class="day Wednesday " id="2017-01-25"><span class="date">25 Jan</span>pseudocode<br/></td>
<td class="day Thursday  lab" id="2017-01-26"><span class="date">26 Jan</span>pseudocode counting squares<br/></td>
<td class="day Friday " id="2017-01-27"><span class="date">27 Jan</span>PyCharm<br/></td>
</tr><tr>
<td class="day Monday " id="2017-01-30"><span class="date">30 Jan</span>course overview with `turtle`{.python}, part 1<br/></td>
<td class="day Wednesday " id="2017-02-01"><span class="date">1 Feb</span>course overview with `turtle`{.python}, part 2<br/><span class="special">Add deadline</span></td>
<td class="day Thursday  lab" id="2017-02-02"><span class="date">2 Feb</span>turtle art contest<br/></td>
<td class="day Friday " id="2017-02-03"><span class="date">3 Feb</span>hello, world!<br/></td>
</tr><tr>
<td class="day Monday " id="2017-02-06"><span class="date">6 Feb</span>variables, values, and operators<br/></td>
<td class="day Wednesday " id="2017-02-08"><span class="date">8 Feb</span>functions -- basics, `def`{.python}<br/></td>
<td class="day Thursday  lab" id="2017-02-09"><span class="date">9 Feb</span><br/></td>
<td class="day Friday " id="2017-02-10"><span class="date">10 Feb</span>functions -- flow of control<br/></td>
</tr><tr>
<td class="day Monday " id="2017-02-13"><span class="date">13 Feb</span>functions -- scope, `global`{.python}<br/></td>
<td class="day Wednesday " id="2017-02-15"><span class="date">15 Feb</span>decisions -- `if`{.python} and `else`{.python}<br/></td>
<td class="day Thursday  lab" id="2017-02-16"><span class="date">16 Feb</span><br/></td>
<td class="day Friday " id="2017-02-17"><span class="date">17 Feb</span>decisions -- `elif`{.python} and logical operators (not on exam 1)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-02-20"><span class="date">20 Feb</span>review<br/></td>
<td class="day Wednesday exam exam" id="2017-02-22"><span class="date">22 Feb</span>exam 1</td>
<td class="day Thursday  lab" id="2017-02-23"><span class="date">23 Feb</span><br/></td>
<td class="day Friday " id="2017-02-24"><span class="date">24 Feb</span>code readability, elegance<br/></td>
</tr><tr>
<td class="day Monday " id="2017-02-27"><span class="date">27 Feb</span>testing<br/></td>
<td class="day Wednesday " id="2017-03-01"><span class="date">1 Mar</span>repeating with `while`{.python}<br/><span class="special">Drop deadline</span></td>
<td class="day Thursday  lab" id="2017-03-02"><span class="date">2 Mar</span><br/></td>
<td class="day Friday " id="2017-03-03"><span class="date">3 Mar</span>composite datatypes -- strings, ranges, lists, tuples<br/></td>
</tr><tr>
<td class="day Monday noclass" id="2017-03-06"><span class="date">6 Mar</span><span class="reason">Spring recess</span></td>
<td class="day Wednesday noclass" id="2017-03-08"><span class="date">8 Mar</span><span class="reason">Spring recess</span></td>
<td class="day Thursday noclass lab" id="2017-03-09"><span class="date">9 Mar</span><span class="reason">Spring recess</span></td>
<td class="day Friday noclass" id="2017-03-10"><span class="date">10 Mar</span><span class="reason">Spring recess</span></td>
</tr><tr>
<td class="day Monday " id="2017-03-13"><span class="date">13 Mar</span>iteration -- the `for`{.python} loop<br/></td>
<td class="day Wednesday " id="2017-03-15"><span class="date">15 Mar</span>methods and mutability -- why `list`{.python} is special<br/></td>
<td class="day Thursday  lab" id="2017-03-16"><span class="date">16 Mar</span><br/></td>
<td class="day Friday " id="2017-03-17"><span class="date">17 Mar</span>applications of lists and strings<br/></td>
</tr><tr>
<td class="day Monday " id="2017-03-20"><span class="date">20 Mar</span>testing list and string code<br/></td>
<td class="day Wednesday " id="2017-03-22"><span class="date">22 Mar</span>flexible indices -- `dict`{.python}<br/></td>
<td class="day Thursday  lab" id="2017-03-23"><span class="date">23 Mar</span><br/></td>
<td class="day Friday " id="2017-03-24"><span class="date">24 Mar</span>reading data -- `open`{.python} and `urllib`{.python}<br/></td>
</tr><tr>
<td class="day Monday " id="2017-03-27"><span class="date">27 Mar</span>understanding data<br/></td>
<td class="day Wednesday " id="2017-03-29"><span class="date">29 Mar</span>more on the data theme<br/></td>
<td class="day Thursday  lab" id="2017-03-30"><span class="date">30 Mar</span><br/></td>
<td class="day Friday " id="2017-03-31"><span class="date">31 Mar</span>polite code -- using `try`{.python} and `except`{.python} (not on exam 2)<br/></td>
</tr><tr>
<td class="day Monday " id="2017-04-03"><span class="date">3 Apr</span>review<br/></td>
<td class="day Wednesday exam" id="2017-04-05"><span class="date">5 Apr</span>exam 2</td>
<td class="day Thursday  lab" id="2017-04-06"><span class="date">6 Apr</span><br/></td>
<td class="day Friday " id="2017-04-07"><span class="date">7 Apr</span>regular expressions<br/></td>
</tr><tr>
<td class="day Monday " id="2017-04-10"><span class="date">10 Apr</span>regular expressions<br/></td>
<td class="day Wednesday " id="2017-04-12"><span class="date">12 Apr</span>regular expressions<br/></td>
<td class="day Thursday  lab" id="2017-04-13"><span class="date">13 Apr</span><br/></td>
<td class="day Friday " id="2017-04-14"><span class="date">14 Apr</span>game design with `gamebox`{.python}<br/></td>
</tr><tr>
<td class="day Monday " id="2017-04-17"><span class="date">17 Apr</span>game design with `gamebox`{.python}<br/></td>
<td class="day Wednesday " id="2017-04-19"><span class="date">19 Apr</span>game design with `gamebox`{.python}<br/></td>
<td class="day Thursday  lab" id="2017-04-20"><span class="date">20 Apr</span><br/></td>
<td class="day Friday " id="2017-04-21"><span class="date">21 Apr</span>image manipulation with `pillow`{.python}<br/></td>
</tr><tr>
<td class="day Monday " id="2017-04-24"><span class="date">24 Apr</span>image manipulation with `pillow`{.python}<br/></td>
<td class="day Wednesday " id="2017-04-26"><span class="date">26 Apr</span>image manipulation with `pillow`{.python}<br/></td>
<td class="day Thursday  lab" id="2017-04-27"><span class="date">27 Apr</span><br/></td>
<td class="day Friday " id="2017-04-28"><span class="date">28 Apr</span>flex day<br/></td>
</tr><tr>
<td class="day Monday " id="2017-05-01"><span class="date">1 May</span>review<br/></td>
</tr></tbody></table>
<table id="age001" class="agenda">
<thead><tr><th>Date</th><th>1110-001 Topic</th></tr></thead>
<tbody><tr id="2017-01-18" class=""><th>18 Jan <br/></th><td>welcome</td></tr>
<tr id="2017-01-19" class=" lab"><th>19 Jan <br/></th><td>installing Python and PyCharm</td></tr>
<tr id="2017-01-20" class=""><th>20 Jan <br/></th><td>from requirements to software</td></tr>
<tr id="2017-01-23" class=""><th>23 Jan <br/></th><td>ambiguity</td></tr>
<tr id="2017-01-25" class=""><th>25 Jan <br/></th><td>pseudocode</td></tr>
<tr id="2017-01-26" class=" lab"><th>26 Jan <br/></th><td>pseudocode counting squares</td></tr>
<tr id="2017-01-27" class=""><th>27 Jan <br/></th><td>PyCharm</td></tr>
<tr id="2017-01-30" class=""><th>30 Jan <br/></th><td>course overview with `turtle`{.python}, part 1</td></tr>
<tr id="2017-02-01" class=""><th>1 Feb <br/><span class="special">Add deadline</span></th><td>course overview with `turtle`{.python}, part 2</td></tr>
<tr id="2017-02-02" class=" lab"><th>2 Feb <br/></th><td>turtle art contest</td></tr>
<tr id="2017-02-03" class=""><th>3 Feb <br/></th><td>hello, world!</td></tr>
<tr id="2017-02-06" class=""><th>6 Feb <br/></th><td>variables, values, and operators</td></tr>
<tr id="2017-02-08" class=""><th>8 Feb <br/></th><td>functions -- basics, `def`{.python}</td></tr>
<tr id="2017-02-09" class=" lab"><th>9 Feb <br/></th><td></td></tr>
<tr id="2017-02-10" class=""><th>10 Feb <br/></th><td>functions -- flow of control</td></tr>
<tr id="2017-02-13" class=""><th>13 Feb <br/></th><td>functions -- scope, `global`{.python}</td></tr>
<tr id="2017-02-15" class=""><th>15 Feb <br/></th><td>decisions -- `if`{.python} and `else`{.python}</td></tr>
<tr id="2017-02-16" class=" lab"><th>16 Feb <br/></th><td></td></tr>
<tr id="2017-02-17" class=""><th>17 Feb <br/></th><td>decisions -- `elif`{.python} and logical operators (not on exam 1)</td></tr>
<tr id="2017-02-20" class=""><th>20 Feb <br/></th><td>review</td></tr>
<tr id="2017-02-22" class="exam exam"><th>22 Feb </th><td>exam 1</td></tr>
<tr id="2017-02-23" class=" lab"><th>23 Feb <br/></th><td></td></tr>
<tr id="2017-02-24" class=""><th>24 Feb <br/></th><td>code readability, elegance</td></tr>
<tr id="2017-02-27" class=""><th>27 Feb <br/></th><td>testing</td></tr>
<tr id="2017-03-01" class=""><th>1 Mar <br/><span class="special">Drop deadline</span></th><td>repeating with `while`{.python}</td></tr>
<tr id="2017-03-02" class=" lab"><th>2 Mar <br/></th><td></td></tr>
<tr id="2017-03-03" class=""><th>3 Mar <br/></th><td>composite datatypes -- strings, ranges, lists, tuples</td></tr>
<tr id="2017-03-06" class="noclass"><th>6 Mar </th><td><span class="reason">Spring recess</span></td></tr>
<tr id="2017-03-08" class="noclass"><th>8 Mar </th><td><span class="reason">Spring recess</span></td></tr>
<tr id="2017-03-09" class="noclass lab"><th>9 Mar </th><td><span class="reason">Spring recess</span></td></tr>
<tr id="2017-03-10" class="noclass"><th>10 Mar </th><td><span class="reason">Spring recess</span></td></tr>
<tr id="2017-03-13" class=""><th>13 Mar <br/></th><td>iteration -- the `for`{.python} loop</td></tr>
<tr id="2017-03-15" class=""><th>15 Mar <br/></th><td>methods and mutability -- why `list`{.python} is special</td></tr>
<tr id="2017-03-16" class=" lab"><th>16 Mar <br/></th><td></td></tr>
<tr id="2017-03-17" class=""><th>17 Mar <br/></th><td>applications of lists and strings</td></tr>
<tr id="2017-03-20" class=""><th>20 Mar <br/></th><td>testing list and string code</td></tr>
<tr id="2017-03-22" class=""><th>22 Mar <br/></th><td>flexible indices -- `dict`{.python}</td></tr>
<tr id="2017-03-23" class=" lab"><th>23 Mar <br/></th><td></td></tr>
<tr id="2017-03-24" class=""><th>24 Mar <br/></th><td>reading data -- `open`{.python} and `urllib`{.python}</td></tr>
<tr id="2017-03-27" class=""><th>27 Mar <br/></th><td>understanding data</td></tr>
<tr id="2017-03-29" class=""><th>29 Mar <br/></th><td>more on the data theme</td></tr>
<tr id="2017-03-30" class=" lab"><th>30 Mar <br/></th><td></td></tr>
<tr id="2017-03-31" class=""><th>31 Mar <br/></th><td>polite code -- using `try`{.python} and `except`{.python} (not on exam 2)</td></tr>
<tr id="2017-04-03" class=""><th>3 Apr <br/></th><td>review</td></tr>
<tr id="2017-04-05" class="exam"><th>5 Apr </th><td>exam 2</td></tr>
<tr id="2017-04-06" class=" lab"><th>6 Apr <br/></th><td></td></tr>
<tr id="2017-04-07" class=""><th>7 Apr <br/></th><td>regular expressions</td></tr>
<tr id="2017-04-10" class=""><th>10 Apr <br/></th><td>regular expressions</td></tr>
<tr id="2017-04-12" class=""><th>12 Apr <br/></th><td>regular expressions</td></tr>
<tr id="2017-04-13" class=" lab"><th>13 Apr <br/></th><td></td></tr>
<tr id="2017-04-14" class=""><th>14 Apr <br/></th><td>game design with `gamebox`{.python}</td></tr>
<tr id="2017-04-17" class=""><th>17 Apr <br/></th><td>game design with `gamebox`{.python}</td></tr>
<tr id="2017-04-19" class=""><th>19 Apr <br/></th><td>game design with `gamebox`{.python}</td></tr>
<tr id="2017-04-20" class=" lab"><th>20 Apr <br/></th><td></td></tr>
<tr id="2017-04-21" class=""><th>21 Apr <br/></th><td>image manipulation with `pillow`{.python}</td></tr>
<tr id="2017-04-24" class=""><th>24 Apr <br/></th><td>image manipulation with `pillow`{.python}</td></tr>
<tr id="2017-04-26" class=""><th>26 Apr <br/></th><td>image manipulation with `pillow`{.python}</td></tr>
<tr id="2017-04-27" class=" lab"><th>27 Apr <br/></th><td></td></tr>
<tr id="2017-04-28" class=""><th>28 Apr <br/></th><td>flex day</td></tr>
<tr id="2017-05-01" class=""><th>1 May <br/></th><td>review</td></tr>
</tbody></table>
<table id="cal002" class="calender">
<thead><tr><th>Monday</th><th>Wednesday</th><th>Thursday</th><th>Friday</th></tr></thead>
<tbody><tr><td/>
<td class="day Wednesday " id="2017-01-18"><span class="date">18 Jan</span>welcome<br/></td>
<td class="day Thursday  lab" id="2017-01-19"><span class="date">19 Jan</span>installing Python and PyCharm<br/></td>
<td class="day Friday " id="2017-01-20"><span class="date">20 Jan</span><br/></td>
</tr><tr>
<td class="day Monday " id="2017-01-23"><span class="date">23 Jan</span><br/></td>
<td class="day Wednesday " id="2017-01-25"><span class="date">25 Jan</span><br/></td>
<td class="day Thursday  lab" id="2017-01-26"><span class="date">26 Jan</span>pseudocode counting squares<br/></td>
<td class="day Friday " id="2017-01-27"><span class="date">27 Jan</span><br/></td>
</tr><tr>
<td class="day Monday " id="2017-01-30"><span class="date">30 Jan</span><br/></td>
<td class="day Wednesday " id="2017-02-01"><span class="date">1 Feb</span><br/><span class="special">Add deadline</span></td>
<td class="day Thursday  lab" id="2017-02-02"><span class="date">2 Feb</span>turtle art contest<br/></td>
<td class="day Friday " id="2017-02-03"><span class="date">3 Feb</span><br/></td>
</tr><tr>
<td class="day Monday " id="2017-02-06"><span class="date">6 Feb</span><br/></td>
<td class="day Wednesday " id="2017-02-08"><span class="date">8 Feb</span><br/></td>
<td class="day Thursday  lab" id="2017-02-09"><span class="date">9 Feb</span><br/></td>
<td class="day Friday " id="2017-02-10"><span class="date">10 Feb</span><br/></td>
</tr><tr>
<td class="day Monday " id="2017-02-13"><span class="date">13 Feb</span><br/></td>
<td class="day Wednesday " id="2017-02-15"><span class="date">15 Feb</span><br/></td>
<td class="day Thursday  lab" id="2017-02-16"><span class="date">16 Feb</span><br/></td>
<td class="day Friday " id="2017-02-17"><span class="date">17 Feb</span><br/></td>
</tr><tr>
<td class="day Monday " id="2017-02-20"><span class="date">20 Feb</span>review<br/></td>
<td class="day Wednesday exam exam" id="2017-02-22"><span class="date">22 Feb</span>exam 1</td>
<td class="day Thursday  lab" id="2017-02-23"><span class="date">23 Feb</span><br/></td>
<td class="day Friday " id="2017-02-24"><span class="date">24 Feb</span><br/></td>
</tr><tr>
<td class="day Monday " id="2017-02-27"><span class="date">27 Feb</span><br/></td>
<td class="day Wednesday " id="2017-03-01"><span class="date">1 Mar</span><br/><span class="special">Drop deadline</span></td>
<td class="day Thursday  lab" id="2017-03-02"><span class="date">2 Mar</span><br/></td>
<td class="day Friday " id="2017-03-03"><span class="date">3 Mar</span><br/></td>
</tr><tr>
<td class="day Monday noclass" id="2017-03-06"><span class="date">6 Mar</span><span class="reason">Spring recess</span></td>
<td class="day Wednesday noclass" id="2017-03-08"><span class="date">8 Mar</span><span class="reason">Spring recess</span></td>
<td class="day Thursday noclass lab" id="2017-03-09"><span class="date">9 Mar</span><span class="reason">Spring recess</span></td>
<td class="day Friday noclass" id="2017-03-10"><span class="date">10 Mar</span><span class="reason">Spring recess</span></td>
</tr><tr>
<td class="day Monday " id="2017-03-13"><span class="date">13 Mar</span><br/></td>
<td class="day Wednesday " id="2017-03-15"><span class="date">15 Mar</span><br/></td>
<td class="day Thursday  lab" id="2017-03-16"><span class="date">16 Mar</span><br/></td>
<td class="day Friday " id="2017-03-17"><span class="date">17 Mar</span><br/></td>
</tr><tr>
<td class="day Monday " id="2017-03-20"><span class="date">20 Mar</span><br/></td>
<td class="day Wednesday " id="2017-03-22"><span class="date">22 Mar</span><br/></td>
<td class="day Thursday  lab" id="2017-03-23"><span class="date">23 Mar</span><br/></td>
<td class="day Friday " id="2017-03-24"><span class="date">24 Mar</span><br/></td>
</tr><tr>
<td class="day Monday " id="2017-03-27"><span class="date">27 Mar</span><br/></td>
<td class="day Wednesday " id="2017-03-29"><span class="date">29 Mar</span><br/></td>
<td class="day Thursday  lab" id="2017-03-30"><span class="date">30 Mar</span><br/></td>
<td class="day Friday " id="2017-03-31"><span class="date">31 Mar</span><br/></td>
</tr><tr>
<td class="day Monday " id="2017-04-03"><span class="date">3 Apr</span>review<br/></td>
<td class="day Wednesday exam" id="2017-04-05"><span class="date">5 Apr</span>exam 2</td>
<td class="day Thursday  lab" id="2017-04-06"><span class="date">6 Apr</span><br/></td>
<td class="day Friday " id="2017-04-07"><span class="date">7 Apr</span><br/></td>
</tr><tr>
<td class="day Monday " id="2017-04-10"><span class="date">10 Apr</span><br/></td>
<td class="day Wednesday " id="2017-04-12"><span class="date">12 Apr</span><br/></td>
<td class="day Thursday  lab" id="2017-04-13"><span class="date">13 Apr</span><br/></td>
<td class="day Friday " id="2017-04-14"><span class="date">14 Apr</span>game design with `gamebox`{.python}<br/></td>
</tr><tr>
<td class="day Monday " id="2017-04-17"><span class="date">17 Apr</span>game design with `gamebox`{.python}<br/></td>
<td class="day Wednesday " id="2017-04-19"><span class="date">19 Apr</span>game design with `gamebox`{.python}<br/></td>
<td class="day Thursday  lab" id="2017-04-20"><span class="date">20 Apr</span><br/></td>
<td class="day Friday " id="2017-04-21"><span class="date">21 Apr</span>image manipulation with `pillow`{.python}<br/></td>
</tr><tr>
<td class="day Monday " id="2017-04-24"><span class="date">24 Apr</span>image manipulation with `pillow`{.python}<br/></td>
<td class="day Wednesday " id="2017-04-26"><span class="date">26 Apr</span>image manipulation with `pillow`{.python}<br/></td>
<td class="day Thursday  lab" id="2017-04-27"><span class="date">27 Apr</span><br/></td>
<td class="day Friday " id="2017-04-28"><span class="date">28 Apr</span>flex day<br/></td>
</tr><tr>
<td class="day Monday " id="2017-05-01"><span class="date">1 May</span>review<br/></td>
</tr></tbody></table>
<table id="age002" class="agenda">
<thead><tr><th>Date</th><th>1110-002 Topic</th></tr></thead>
<tbody><tr id="2017-01-18" class=""><th>18 Jan <br/></th><td>welcome</td></tr>
<tr id="2017-01-19" class=" lab"><th>19 Jan <br/></th><td>installing Python and PyCharm</td></tr>
<tr id="2017-01-20" class=""><th>20 Jan <br/></th><td></td></tr>
<tr id="2017-01-23" class=""><th>23 Jan <br/></th><td></td></tr>
<tr id="2017-01-25" class=""><th>25 Jan <br/></th><td></td></tr>
<tr id="2017-01-26" class=" lab"><th>26 Jan <br/></th><td>pseudocode counting squares</td></tr>
<tr id="2017-01-27" class=""><th>27 Jan <br/></th><td></td></tr>
<tr id="2017-01-30" class=""><th>30 Jan <br/></th><td></td></tr>
<tr id="2017-02-01" class=""><th>1 Feb <br/><span class="special">Add deadline</span></th><td></td></tr>
<tr id="2017-02-02" class=" lab"><th>2 Feb <br/></th><td>turtle art contest</td></tr>
<tr id="2017-02-03" class=""><th>3 Feb <br/></th><td></td></tr>
<tr id="2017-02-06" class=""><th>6 Feb <br/></th><td></td></tr>
<tr id="2017-02-08" class=""><th>8 Feb <br/></th><td></td></tr>
<tr id="2017-02-09" class=" lab"><th>9 Feb <br/></th><td></td></tr>
<tr id="2017-02-10" class=""><th>10 Feb <br/></th><td></td></tr>
<tr id="2017-02-13" class=""><th>13 Feb <br/></th><td></td></tr>
<tr id="2017-02-15" class=""><th>15 Feb <br/></th><td></td></tr>
<tr id="2017-02-16" class=" lab"><th>16 Feb <br/></th><td></td></tr>
<tr id="2017-02-17" class=""><th>17 Feb <br/></th><td></td></tr>
<tr id="2017-02-20" class=""><th>20 Feb <br/></th><td>review</td></tr>
<tr id="2017-02-22" class="exam exam"><th>22 Feb </th><td>exam 1</td></tr>
<tr id="2017-02-23" class=" lab"><th>23 Feb <br/></th><td></td></tr>
<tr id="2017-02-24" class=""><th>24 Feb <br/></th><td></td></tr>
<tr id="2017-02-27" class=""><th>27 Feb <br/></th><td></td></tr>
<tr id="2017-03-01" class=""><th>1 Mar <br/><span class="special">Drop deadline</span></th><td></td></tr>
<tr id="2017-03-02" class=" lab"><th>2 Mar <br/></th><td></td></tr>
<tr id="2017-03-03" class=""><th>3 Mar <br/></th><td></td></tr>
<tr id="2017-03-06" class="noclass"><th>6 Mar </th><td><span class="reason">Spring recess</span></td></tr>
<tr id="2017-03-08" class="noclass"><th>8 Mar </th><td><span class="reason">Spring recess</span></td></tr>
<tr id="2017-03-09" class="noclass lab"><th>9 Mar </th><td><span class="reason">Spring recess</span></td></tr>
<tr id="2017-03-10" class="noclass"><th>10 Mar </th><td><span class="reason">Spring recess</span></td></tr>
<tr id="2017-03-13" class=""><th>13 Mar <br/></th><td></td></tr>
<tr id="2017-03-15" class=""><th>15 Mar <br/></th><td></td></tr>
<tr id="2017-03-16" class=" lab"><th>16 Mar <br/></th><td></td></tr>
<tr id="2017-03-17" class=""><th>17 Mar <br/></th><td></td></tr>
<tr id="2017-03-20" class=""><th>20 Mar <br/></th><td></td></tr>
<tr id="2017-03-22" class=""><th>22 Mar <br/></th><td></td></tr>
<tr id="2017-03-23" class=" lab"><th>23 Mar <br/></th><td></td></tr>
<tr id="2017-03-24" class=""><th>24 Mar <br/></th><td></td></tr>
<tr id="2017-03-27" class=""><th>27 Mar <br/></th><td></td></tr>
<tr id="2017-03-29" class=""><th>29 Mar <br/></th><td></td></tr>
<tr id="2017-03-30" class=" lab"><th>30 Mar <br/></th><td></td></tr>
<tr id="2017-03-31" class=""><th>31 Mar <br/></th><td></td></tr>
<tr id="2017-04-03" class=""><th>3 Apr <br/></th><td>review</td></tr>
<tr id="2017-04-05" class="exam"><th>5 Apr </th><td>exam 2</td></tr>
<tr id="2017-04-06" class=" lab"><th>6 Apr <br/></th><td></td></tr>
<tr id="2017-04-07" class=""><th>7 Apr <br/></th><td></td></tr>
<tr id="2017-04-10" class=""><th>10 Apr <br/></th><td></td></tr>
<tr id="2017-04-12" class=""><th>12 Apr <br/></th><td></td></tr>
<tr id="2017-04-13" class=" lab"><th>13 Apr <br/></th><td></td></tr>
<tr id="2017-04-14" class=""><th>14 Apr <br/></th><td>game design with `gamebox`{.python}</td></tr>
<tr id="2017-04-17" class=""><th>17 Apr <br/></th><td>game design with `gamebox`{.python}</td></tr>
<tr id="2017-04-19" class=""><th>19 Apr <br/></th><td>game design with `gamebox`{.python}</td></tr>
<tr id="2017-04-20" class=" lab"><th>20 Apr <br/></th><td></td></tr>
<tr id="2017-04-21" class=""><th>21 Apr <br/></th><td>image manipulation with `pillow`{.python}</td></tr>
<tr id="2017-04-24" class=""><th>24 Apr <br/></th><td>image manipulation with `pillow`{.python}</td></tr>
<tr id="2017-04-26" class=""><th>26 Apr <br/></th><td>image manipulation with `pillow`{.python}</td></tr>
<tr id="2017-04-27" class=" lab"><th>27 Apr <br/></th><td></td></tr>
<tr id="2017-04-28" class=""><th>28 Apr <br/></th><td>flex day</td></tr>
<tr id="2017-05-01" class=""><th>1 May <br/></th><td>review</td></tr>
</tbody></table>
<table id="cal1111" class="calender">
<thead><tr><th>Monday</th><th>Wednesday</th></tr></thead>
<tbody><tr><td/>
<td class="day Wednesday " id="2017-01-18"><span class="date">18 Jan</span>welcome<br/></td>
</tr><tr>
<td class="day Monday " id="2017-01-23"><span class="date">23 Jan</span><br/></td>
<td class="day Wednesday " id="2017-01-25"><span class="date">25 Jan</span><br/></td>
</tr><tr>
<td class="day Monday " id="2017-01-30"><span class="date">30 Jan</span><br/></td>
<td class="day Wednesday " id="2017-02-01"><span class="date">1 Feb</span><br/><span class="special">Add deadline</span></td>
</tr><tr>
<td class="day Monday " id="2017-02-06"><span class="date">6 Feb</span><br/></td>
<td class="day Wednesday " id="2017-02-08"><span class="date">8 Feb</span><br/></td>
</tr><tr>
<td class="day Monday " id="2017-02-13"><span class="date">13 Feb</span><br/></td>
<td class="day Wednesday " id="2017-02-15"><span class="date">15 Feb</span><br/></td>
</tr><tr>
<td class="day Monday " id="2017-02-20"><span class="date">20 Feb</span>review<br/></td>
<td class="day Wednesday exam exam" id="2017-02-22"><span class="date">22 Feb</span>exam 1</td>
</tr><tr>
<td class="day Monday " id="2017-02-27"><span class="date">27 Feb</span><br/></td>
<td class="day Wednesday " id="2017-03-01"><span class="date">1 Mar</span><br/><span class="special">Drop deadline</span></td>
</tr><tr>
<td class="day Monday noclass" id="2017-03-06"><span class="date">6 Mar</span><span class="reason">Spring recess</span></td>
<td class="day Wednesday noclass" id="2017-03-08"><span class="date">8 Mar</span><span class="reason">Spring recess</span></td>
</tr><tr>
<td class="day Monday " id="2017-03-13"><span class="date">13 Mar</span><br/></td>
<td class="day Wednesday " id="2017-03-15"><span class="date">15 Mar</span><br/></td>
</tr><tr>
<td class="day Monday " id="2017-03-20"><span class="date">20 Mar</span><br/></td>
<td class="day Wednesday " id="2017-03-22"><span class="date">22 Mar</span><br/></td>
</tr><tr>
<td class="day Monday " id="2017-03-27"><span class="date">27 Mar</span><br/></td>
<td class="day Wednesday " id="2017-03-29"><span class="date">29 Mar</span><br/></td>
</tr><tr>
<td class="day Monday " id="2017-04-03"><span class="date">3 Apr</span>review<br/></td>
<td class="day Wednesday exam" id="2017-04-05"><span class="date">5 Apr</span>exam 2</td>
</tr><tr>
<td class="day Monday " id="2017-04-10"><span class="date">10 Apr</span><br/></td>
<td class="day Wednesday " id="2017-04-12"><span class="date">12 Apr</span><br/></td>
</tr><tr>
<td class="day Monday " id="2017-04-17"><span class="date">17 Apr</span>game design with `gamebox`{.python}<br/></td>
<td class="day Wednesday " id="2017-04-19"><span class="date">19 Apr</span>game design with `gamebox`{.python}<br/></td>
</tr><tr>
<td class="day Monday " id="2017-04-24"><span class="date">24 Apr</span>image manipulation with `pillow`{.python}<br/></td>
<td class="day Wednesday " id="2017-04-26"><span class="date">26 Apr</span>image manipulation with `pillow`{.python}<br/></td>
</tr><tr>
<td class="day Monday " id="2017-05-01"><span class="date">1 May</span>review<br/></td>
</tr></tbody></table>
<table id="age1111" class="agenda">
<thead><tr><th>Date</th><th>1111 Topic</th></tr></thead>
<tbody><tr id="2017-01-18" class=""><th>18 Jan <br/></th><td>welcome</td></tr>
<tr id="2017-01-23" class=""><th>23 Jan <br/></th><td></td></tr>
<tr id="2017-01-25" class=""><th>25 Jan <br/></th><td></td></tr>
<tr id="2017-01-30" class=""><th>30 Jan <br/></th><td></td></tr>
<tr id="2017-02-01" class=""><th>1 Feb <br/><span class="special">Add deadline</span></th><td></td></tr>
<tr id="2017-02-06" class=""><th>6 Feb <br/></th><td></td></tr>
<tr id="2017-02-08" class=""><th>8 Feb <br/></th><td></td></tr>
<tr id="2017-02-13" class=""><th>13 Feb <br/></th><td></td></tr>
<tr id="2017-02-15" class=""><th>15 Feb <br/></th><td></td></tr>
<tr id="2017-02-20" class=""><th>20 Feb <br/></th><td>review</td></tr>
<tr id="2017-02-22" class="exam exam"><th>22 Feb </th><td>exam 1</td></tr>
<tr id="2017-02-27" class=""><th>27 Feb <br/></th><td></td></tr>
<tr id="2017-03-01" class=""><th>1 Mar <br/><span class="special">Drop deadline</span></th><td></td></tr>
<tr id="2017-03-06" class="noclass"><th>6 Mar </th><td><span class="reason">Spring recess</span></td></tr>
<tr id="2017-03-08" class="noclass"><th>8 Mar </th><td><span class="reason">Spring recess</span></td></tr>
<tr id="2017-03-13" class=""><th>13 Mar <br/></th><td></td></tr>
<tr id="2017-03-15" class=""><th>15 Mar <br/></th><td></td></tr>
<tr id="2017-03-20" class=""><th>20 Mar <br/></th><td></td></tr>
<tr id="2017-03-22" class=""><th>22 Mar <br/></th><td></td></tr>
<tr id="2017-03-27" class=""><th>27 Mar <br/></th><td></td></tr>
<tr id="2017-03-29" class=""><th>29 Mar <br/></th><td></td></tr>
<tr id="2017-04-03" class=""><th>3 Apr <br/></th><td>review</td></tr>
<tr id="2017-04-05" class="exam"><th>5 Apr </th><td>exam 2</td></tr>
<tr id="2017-04-10" class=""><th>10 Apr <br/></th><td></td></tr>
<tr id="2017-04-12" class=""><th>12 Apr <br/></th><td></td></tr>
<tr id="2017-04-17" class=""><th>17 Apr <br/></th><td>game design with `gamebox`{.python}</td></tr>
<tr id="2017-04-19" class=""><th>19 Apr <br/></th><td>game design with `gamebox`{.python}</td></tr>
<tr id="2017-04-24" class=""><th>24 Apr <br/></th><td>image manipulation with `pillow`{.python}</td></tr>
<tr id="2017-04-26" class=""><th>26 Apr <br/></th><td>image manipulation with `pillow`{.python}</td></tr>
<tr id="2017-05-01" class=""><th>1 May <br/></th><td>review</td></tr>
</tbody></table>
<script>rehide()</script>
