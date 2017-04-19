---
title: "Lab 13: Email Finder"
...


# Attendance

We will be taking roll in lab each week! Please come to your assigned lab to be counted present!

Each lab TAs are empowered to select their own method of taking roll.
Please follow your lab TA's instructions.  
They may dock points if you  are excessively late or leave unusually early.

# Pairing

For this and all subsequent labs, you will work in pairs.
This need not be your game project partner, though it may be if you are in the same lab and wish to work together on this task too.

# Activity

Spammers sometimes search the web for email addresses.
People who want people to cantact them, but not spammers, sometimes post their addresses in an obfuscated form.
Spammers write programs to detect this obfuscation.
People come up with new ones.
Etc.

In this lab, you'll practice regular expressions by harvesting email addresses from a website.

## Example page

<http://cs1110.cs.virginia.edu/emails.html>

As a reminder, you can read it line-by-line using 

````python
import urllib.request

stream = urllib.request.urlopen('http://cs1110.cs.virginia.edu/emails.html')

for line in stream:
    decoded = line.decode('UTF-8').strip()
    # add code here
````

## Your code

Add code that finds email addresses, and prints them out.
Print only email addresses from the website given, one per line, with no duplicates.
You should not hard-code: if we change the content of the webpage, your output should change.

Example output for <http://cs1110.cs.virginia.edu/emails.html> might be

````
basic@virginia.edu
link-only@virginia.edu
multi-domain@cs.virginia.edu
Mr.N0body@cand3lwick-burnERS.rentals
a@b.ca
no-at-sign@virginia.edu
no-at-or-dot@virginia.edu
first.last.name@cs.virginia.edu
with-parenthesis@Virginia.EDU
added-words1@virginia.edu
added-words2@virginia.edu
may.end@with-a-period.com
underscore@virginia.edu
reverse@virginia.edu
JohnDoe@virginia.edu
markdown@virginia.edu
````

See how many you can get (without having non-addresses).
We don't expect many of you to get them all...

Most of these will be easier with regular expressions than without, but don't forget about string methods like `replace` as well.


## Submission

**At least one partner** should submit one .py file named `emailhunt.py` to Archimedes (the submission system):
[https://archimedes.cs.virginia.edu/cs1110/](https://archimedes.cs.virginia.edu/cs1110/).
Please put **all partners' ids** in comments at the top of the file.
