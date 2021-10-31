from hackthebox import *
from getpass import getpass
from pwn import *
import argparse
import os
import pathlib
import re

def _LEN(value):
    if value != None:
        return(len(value))
    else:
        return(0)


def green(text):
    return(f"\033[92m{text}\033[0m")


class Writeup():
    def __init__(self, Args, Client):
        self.Machine_ID = Args.machine
        self.Challenge_ID = Args.challenge
        self.Client = Client
        
        if os.name == "posix":
            self.Home = os.getenv("HOME") 
        elif os.name == "nt":
            self.Home = os.getenv("%UserProfile%")

        if self.Machine_ID:
            self.MachineWriteup()

        if self.Challenge_ID:
            self.Challenge()

        if not self.Challenge_ID and not self.Machine_ID:
            log.error("ID Argument Missing")

    def MachineWriteup(self):
        for number in self.Machine_ID:
            try:
                log.progress(f"Machine ID : {number}")
                MachineObj = self.Client.get_machine(number)
                Filename = f"C:\\Users\\Owner\\OneDrive\\Documents\\OneDrive\\Documents\\HTB Writeups\\WriteMeUp\\TimeToWriteUp\\Boxes\\Headers\\{MachineObj.name}.md"

                Filename = re.sub(r'[^\w\-_\. ]', '_', Filename)

                
                if number <= 3:
                    MachineIP = "10.10.10." + str(number)
                else:
                    MachineIP = "10.10.10." + \
                        str(number - 3)  # ! May Need Fixing

                with open(Filename, "w+") as f:
                    Content = f"HTB - {MachineObj.name.title()} [{MachineObj.difficulty}]\n"
                    Content += f"**Name** : {MachineObj.name}\n"
                    Content += f"**Difficulty** : {MachineObj.difficulty}\n"
                    Content += f"**OS** : {MachineObj.os}\n"
                    Content += f'**URL** : [{"https://app.hackthebox.eu/machines/" + str(number)}]({"https://app.hackthebox.eu/machines/" + str(self.Machine_ID)})\n'
                    Content += f"**Points** : {MachineObj.points}\n"
                    Content += f"**Stars** : {MachineObj.stars}\n"
                    Content += f"**Internal IP** : {MachineIP}\n"
                    f.write(Content)

                log.progress(f"    Written to {Filename}\n")
            except errors.NotFoundException:
                log.info("Machine with this ID does not exist.\n")

    def Challenge(self):
        for number in self.Challenge_ID:
            try:
                log.progress(f"Challenge ID : {number}")
                ChallengeObj = self.Client.get_challenge(number)

                Filename = f'C:\\Users\\Owner\\OneDrive\\Documents\\OneDrive\\Documents\\HTB Writeups\\WriteMeUp\\TimeToWriteUp\\Challenges\\Headers\\{ChallengeObj.name}.md'
                
                Filename = re.sub(r'[^\w\-_\. ]', '_', Filename)    
                with open(Filename, "a+", encoding='utf-8') as f:
                    Content = f"HTB - {ChallengeObj.name.title()} [{ChallengeObj.category}]\n\n"
                    Content += f"```\n**Name** : {ChallengeObj.name}\n"
                    Content += f"**Category** : {ChallengeObj.category}\n"
                    Content += f"**Difficulty** : {ChallengeObj.difficulty}\n"
                    Content += f"**Description** : `{ChallengeObj.description}`\n"
                    Content += f'**URL** : [{"https://app.hackthebox.eu/challenge/" + str(number)}]({"https://app.hackthebox.eu/challenge/" + str(number)})\n'
                    Content += f"**Points** : {ChallengeObj.points}\n```"
                    f.write(Content)

                log.success(f"    Written to {Filename}")
            except errors.NotFoundException:
                log.info("Challenge with this ID does not exist.")


# Argparse
Parser = argparse.ArgumentParser()
Parser.add_argument("-challenge", "-c", metavar="", help="Use this to run writeup creation on a certain challenge",
                    action="store", nargs="*", default=None, type=int)
Parser.add_argument("-machine", "-m", metavar="", help="Use this to run writeup creation on a certain machine",
                    action="store", nargs="*", default=None, type=int)
Args = Parser.parse_args()

if __name__ == "__main__":
    # GetPass Securely
    # Password = getpass(f"\033[93mInput your Password > \033[0m")
    Client = HTBClient(email="", password=Password)
    log.info(f"Authenticated as {green(Client.user.name)}")
    c, m = _LEN(Args.challenge), _LEN(Args.machine)
    log.info(f"Processing {green(c)} Challenges and {green(m)} Machines")
    Writeup(Args, Client)
