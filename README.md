# Gmail Alias Generator

<a href="#how-work">aa</a>

# a
# b
# b
# c
# d
# e
# f
# g
# h

## How does it work? <span id="how-work"></span>

**Adding dots in between the username**<br>
&nbsp;&nbsp;-> When receiving mails, Google removes all dots from your address<br>
&nbsp;&nbsp;-> This is why we can add random dots accross the address to "scramble it"<br>
&nbsp;&nbsp;-> In this case we have the following rules<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Don't add dots at the beginning or end and only before the @ sign<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Don't surpass the threshold of 43 % dots<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Don't have 2 dots in a row (exam..ple@​gmail.com)<br>
&nbsp;&nbsp;-> Example: exam.plema.il@​gmail.com forwards to example.mail@​gmail.com
 
**Alternating between domains**
<br>&nbsp;&nbsp;-> @gmail.com and @googlemail.com are basically the same
<br>&nbsp;&nbsp;-> We can still use both addresses on one service
<br>&nbsp;&nbsp;-> Meaning we essentially double our alias amount
<br>&nbsp;&nbsp;-> Example: example.mail​@googlemail.com forwards to example.mail@​gmail.com

**Adding a + at the end of our username**
<br>&nbsp;&nbsp;-> Gmail also has a built-in functionality for alias generation
<br>&nbsp;&nbsp;-> We can add a + sign at the end of our username and everything between it and the @ will be ignored
<br>&nbsp;&nbsp;-> Example: example.mail+g34d​@gmail.com forwards to example.mail​@gmail.com
 
**Examples**
<br>&nbsp;&nbsp;-> e.xamp.lemai.l+89dfgascb@​googlemail.com forwards to example.mail@​gmail.com
<br>&nbsp;&nbsp;-> m.y.c.ooladdres.s+xyz69@​gmail.com forwards to my.cool.address@​gmail.com
