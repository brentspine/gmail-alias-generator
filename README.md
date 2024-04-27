# Gmail Alias Generator

Your Gmail address can be "scrambled". This allows you to have 10k or up to unlimited addresses linked to one inbox. This is done by adding periods or plus signs at the end of the username. 

This repository helps you generate a big amount of gmail aliases automatically. 

## Table of Contents
**[1. How do I run it?](#how-to-run)**<br>
**[2. Walkthrough](#walkthrough)**<br>
**[3. How does it work?](#how-does-it-work)**
**[4. Troubleshooting](#trouble-shooting)**

## How do I run it? <span id="how-to-run"></span>
You can run the code via the [Replit](https://replit.com/@brentspine/GenerateGmailAliases) project. Just go the link and click run at the top of the page.

![output-onlinejpgtools](https://github.com/brentspine/gmail-alias-generator/assets/55391576/3d33ecf1-7fd0-48ac-86f2-d73a015d4427)

Alternatively you can clone the code and run it on your own machine.

In the CMD:
```
git clone https://github.com/brentspine/gmail-alias-generator
```

Run it:
```
cd gmail-alias-generator
python main.py
```

## Walkthrough <span id="walkthrough"></span>

After running the program, it asks you to input a **valid** gmail address. You can also keep the field empty if you just want to test functionality

![image](https://github.com/brentspine/gmail-alias-generator/assets/55391576/a7afc421-efea-4e61-8e13-47cd27e5076e)

When the program is done generating your aliases you are prompted with some options you can choose from

![image](https://github.com/brentspine/gmail-alias-generator/assets/55391576/db32e801-caec-4ff6-b13b-c130d5458cc3)

You can generate as many aliases as you want by pressing "1" and pressing enter. <br>
To copy and use your aliases you can either use option 4, which prints all addresses or option 3, which exports them to a file.

If the file you want to export to already exists you can either choose the write or the append mode. The write mode wipes all contents of the file and overwrites them, while the append mode adds the new addresses to the .txt. Important to notice is, that it won't check for duplicates.

![image](https://github.com/brentspine/gmail-alias-generator/assets/55391576/7529133c-219e-435e-a8de-f93465d6b5a9)


## How does it work? <span id="how-does-it-work"></span>

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

## Still have problems or questions? <span id="trouble-shooting"></span>

If you still have problems you can open an [issue](https://github.com/brentspine/gmail-alias-generator/issues) or [contact me](https://linktr.ee/brentspine).

<a href="https://www.buymeacoffee.com/brentspine" rel="nofollow"><img src="https://camo.githubusercontent.com/72239ca228f9e1e3cddaae6c43acb13e22c23f58fdfe78f2c3b44fb9879918d2/68747470733a2f2f696d672e6275796d6561636f666665652e636f6d2f627574746f6e2d6170692f3f746578743d427579206d65206120636f6666656526656d6f6a693d26736c75673d6272656e747370696e6526627574746f6e5f636f6c6f75723d46463546354626666f6e745f636f6c6f75723d66666666666626666f6e745f66616d696c793d436f6d6963266f75746c696e655f636f6c6f75723d30303030303026636f666665655f636f6c6f75723d464644443030" data-canonical-src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&amp;emoji=&amp;slug=brentspine&amp;button_colour=FF5F5F&amp;font_colour=ffffff&amp;font_family=Comic&amp;outline_colour=000000&amp;coffee_colour=FFDD00" style="max-width: 100%;"></a>
