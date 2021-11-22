# HTB Writeup Toolkit
this relies on [clubby's python library](https://github.com/clubby789/htb-api) to work and interface with the HTB API and perform actions based on your input. for instance my challenge writeups generally follow of the following syntax 
<br><br>

### Challenges 
```
HTB - $NAME [$CATEGORY]

**Name** : 
**Category** : 
**Difficulty** : 
**Description** : ``
**URL** : []()
**Points** : 
```
### Machines 
```
HTB - $NAME [$DIFFICULTY]

**Name** : 
**Difficulty** : 
**OS** :
**URL** : []()
**Points** :
**Stars** : 
**Internal IP** 
```


this can often be quite annoying and laborious to type out so HTB Writeup Helper will aim to automate that for me <br>

# How to use Writeup.py 

**By default this will read from the .creds file which should be structed like this**
```
$EMAIL
$PASSWORD
```
The following options are inlcuded in the writeup utility 
```
  -challenge [ ...], -c [ ...]
                        Use this to pass ChallengeIDs in order to generate the attached writeups
  -machine [ ...], -m [ ...]
                        Use this to pass MachineIDs in order to generate the attached writeups
```
 We pass an array of challenge/machine IDs to the writeup utility, this allows us to create an instance of the challenge and use data <br>
 associated with it to generate our writeups.
 
 ```
> python .\Writer.py -c 1 5 89 -m 3 410 2
[*] ======================================================================
[x] Processing .creds file
[x]     Email in .creds file    : [REDACTED]@gmail.com
[x]     Password in .creds file : **************
[*] ======================================================================
[+] Authenticated as [REDACTED]
[*] Processing 3 Challenges and 3 Machines
[*] ======================================================================
[*] Processing Machines : [3, 410, 2]
[x] Machine ID : 3
[+]     Written to Devel.md
[x] Machine ID : 410
[+]     Written to Shibboleth.md
[x] Machine ID : 2
[+]     Written to Legacy.md
[*] Processing Challenges : [1, 5, 89]
[x] Challenge ID : 1
[+]     Written to Crack This_.md
[x] Challenge ID : 5
[+]     Written to Find The Easy Pass.md
[x] Challenge ID : 89
[+]     Written to ExploitedStream.md
 ```
 
 
 
 ## *Disclaimer*
 There is a slight issue with the Machine IPs in that I am unsure of the order that they are generated in, due to HTB having 256 + machines this complications things
 ```
 Devzat 398 -> 10.10.11.118 [1:143]
 Forge 376 -> 10.10.11.111 [1:121]
 Shibboleth 410 -> 10.10.11.124 [1:155]
 ```
