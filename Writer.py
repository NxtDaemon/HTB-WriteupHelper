from hackthebox import *
from getpass import getpass
from pwn import * 
import argparse
import os 

class Writeup():
    def __init__(self, Args, Client):
        self.Machine_ID = Args.machine
        self.Challenge_ID = Args.challenge
        self.Client = Client
        self.Home = os.getenv("HOME")

        if self.Machine_ID and self.Challenge_ID:
            log.Error("Only one flag should be given; please retry with just one")
            exit()
        if self.Machine_ID: self.Machine()
        elif self.Challenge_ID: self.Challenge()

    def Machine(self):
        if self.Machine_ID:
            log.progress("Recived Machine ID")
            Client = self.Client 
            MachineObj = Client.get_machine(self.Machine_ID)
            

            Filename = f"{self.Home}/HTB/Writeups/Machines/{MachineObj.name}.md"
            if self.Machine_ID <= 3:
                MachineIP = "10.10.10." + str(Machine_ID+3)
            else:
                MachineIP = self.Machine_ID - 3
            with open(Filename,"w+") as f:
                f.write(f"""
HTB - {MachineObj.name.capitalize()} [{MachineObj.difficulty}]

**Name** : {MachineObj.name} 
**Difficulty** : {MachineObj.difficulty} 
**OS** : {MachineObj.os}
**URL** : [{"https://app.hackthebox.eu/machines/" + str(self.Machine_ID)}]({"https://app.hackthebox.eu/machines/" + str(self.Machine_ID)})
**Points** : {MachineObj.points}            
**Stars** : {MachineObj.stars}
**Internal IP** : 10.10.10.{MachineIP}""")

            log.progress(f"Outputted to {Filename}")



    def Challenge(self):
        if self.Challenge_ID:
            log.progress("Recieved Challenge ID")
            Client = self.Client
            ChallengeObj = Client.get_challenge(self.Challenge_ID)

            Filename = f"{self.Home}/HTB/Writeups/Challenges/{ChallengeObj.name}.md"
            with open(Filename,"a+") as f:
                f.write(f"""
HTB - {ChallengeObj.name.capitalize()} [{ChallengeObj.category}]

**Name** : {ChallengeObj.name}
**Category** : {ChallengeObj.category}
**Difficulty** : {ChallengeObj.difficulty}
**Description** : `{ChallengeObj.description}`
**URL** : [{"https://app.hackthebox.eu/challenge/" + str(self.Challenge_ID)}]({"https://app.hackthebox.eu/challenge/" + str(self.Challenge_ID)})
**Points** : {ChallengeObj.points}""")

            log.success(f"Outputted to {Filename}")

# Argparse 
Parser = argparse.ArgumentParser()
Parser.add_argument("-challenge","-c",metavar="",help="Use this to run writeup creation on a certain challenge",action="store",type=int,default=None)
Parser.add_argument("-machine","-m",metavar="",help="Use this to run writeup creation on a certain machine",action="store",type=int,default=None)
Args = Parser.parse_args()

if __name__ == "__main__":
    Password = getpass(f"{Color.QuestionColor}Input your Password \n> {Color.RESET}") # GetPass Securely 
    Client = HTBClient(email="",password=Password)
    print(f"Welcome {Client.user}")
    Writeup(Args,Client)
