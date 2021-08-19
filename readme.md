# HTB Writeup Toolkit
this relies on [clubby's python library](https://github.com/clubby789/htb-api) to work and interface with the HTB API and perform actions based on your input. for instance my challenge writeups generally follow of the following syntax 
<br><br>

```
HTB - $NAME [$CATEGORY]

**Name** : 
**Category** : 
**Difficulty** : 
**Description** : ``
**URL** : []()
**Points** : 
```

this can often be quite annoying and laborious to type out so HTB Writeup Helper will aim to automate that for me <br>

Additionally I will Include a second utilitiy dubbed `HTB Tracker` which aims to control will challenges are still outstanding and which still need to be completed it will also serve a todolist of sorts to identify which challenges or machines will need writing up alongside `BatchGrabber` which aims to queue multiple writeups and using timing to ensure the connection doesnt get 427'd 

# Library Correction
for me I had to replace the following line in the pyhackthebox library in file `htb.py` in func `JWT_refresh` line `23` this is suspected to be an issue with the way the HTB API sends tokens in an incorrectly formatted way, likely handled in a similar way for their API access tools 

```
payload = base64.b64decode((token.split('.')[1]) + "==").decode()
```