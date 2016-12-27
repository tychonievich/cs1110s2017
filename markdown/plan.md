<style>
table { border-collapse: collapse; }
thead th { border-bottom: thick solid black; }
.even td { background-color: #eee; }
td:nth-child(3) { background: #eee; }
.even td:nth-child(3) { background: #ddd; }
td, th { padding: 0.5ex; }
.date { display:block; font-size:70%; padding-right:1ex; color:#777;}
td.break:nth-child(n) { color: #aaa; background-color:#ccc; }
td.break:nth-child(n) span.date { color: #777; }
td.strong { background-color: #f70; }

tr:nth-child(3) td:nth-child(1) { border-bottom: thin solid black; }
tr:nth-child(3) td:nth-child(2) { border-bottom: thin solid black; border-right: thin solid black; }
tr:nth-child(2) td:nth-child(3) { border-bottom: thin solid black; }
tr:nth-child(2) td:nth-child(4) { border-bottom: thin solid black; }
</style>

---------------------------------------------------------------------------
Monday              Wednesday           Lab            Friday
------------------- ------------------- -------------- --------------------
*break*             Welcome             installing     Computing:
                                        Python and     design on paper,
                                        PyCharm        algorithms
                                                       in pseudocode,
                                                       implement in Python 
                                                                           
                                                                           
                                                                           
Ambiguity:          Pseudocode:         counting       Pycharm basics
paper airplanes     describing tasks    squares
activity            and testing the                                        
                    descriptions                                           
                                                                           

Turtle:             Turtle:             art contest    Input/Output:       
rapid overview of   rapid overview      using `turtle` `print`, `input`,  
most of course      of most of course                  conversations       
                                                                           

Variables           `def`, parameters   phrasal        numbers, operators
                                        template game  string literals
                                        (like Mad                          
                                        Libs^®^)                        
                                                                           

scope, `global`     `if`, `else`        8-ball         `elif`
                                                                           
                                                                           
                                                                           

**review**          **exam**            bug hunt:      testing:
                                        hidden code    selecting good       
                                        has logic      test cases          
                                        errors to find                     

`str`, `len`,       split, join, `for`, string puzzles `file` basics:
and methods         and lists from      to be solved   reading and
                    strings             using string   writing strings;
                                        methods        `float()`                    


*break*             *break*             *break*        *break*


`for i in range`,   input validation    guess again:   `list` functions
`while`                                 a stupid kind  and methods
                                        of guessing                        
                                        game                               

loops and design    things go wrong;    bug hunt 2:    `urllib`
                    `try`/`except`,     now with more
                    especially with     kinds of errors                    
                    files                                                  
                                                                           

file formats, CSV   basic regex,        weather.gov:   reading HTML, XML:
                    wildcards           building a     nested tags
                    `.*`, `[a-z]*`      weather app               
                                                                           
                                                                           

**review**          **exam**            Lou's List     `dict`: key-value
                                                       storage             
                                                                           
                                                                           

gamebox             gamebox             flappy birds   +1 topic
                                                                           
                                                                           
                                                                           

images              images              sketcher       +1 topic
                                                                           
                                                                           
                                                                           

+1 topic            +1 topic            review game    +1 topic
                                                                           
                                                                           
                                                                           

**review**          *break*             *break*        *break*

--------------------------------------------------------------------------


By week:

1.   Welcome (W)
2.   Big ideas, pseudocode (FMW)
3.   Overview of course via turtle (FMW)
4.   variables, functions (FMW)
5.   numbers, scope, conditionals (FMWF)
6.   **exam**
7.   testing, `str`, `file` (FMWF)
8.   *spring break*
9.   `while`, validation (MW)
10.  `for`, loops, `try` (FMW)
11.  `urllib`, parsing   (FMWF)
12.  **exam**
13.  games + dict
14.  images + 
15.  extra (FMWF)
16. review

<script>
var tds = document.getElementsByTagName('td');
var start = new Date(2017,0,16);
for(var i = 0; i < tds.length; i+=1) {
     var td = tds[i];
     if (td.innerHTML == '<em>break</em>') {
          td.setAttribute('class','break');
     }
     if (td.innerHTML.substring(0,8) == '<strong>') {
          td.setAttribute('class','strong');
     }
     var show = start.toString().split(' ').slice(1,3).join(' ');
     td.innerHTML = '<span class="date">'+show+'</span>'+td.innerHTML;

     if (start.getDay() == 1) start.setDate(start.getDate()+2);
     else if (start.getDay() == 3) start.setDate(start.getDate()+1);
     else if (start.getDay() == 4) start.setDate(start.getDate()+1);
     else if (start.getDay() == 5) start.setDate(start.getDate()+3);
     else break;
}
</script>
