---
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


