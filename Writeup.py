from hackthebox import *
from getpass import getpass
from pwn import *
import argparse
import os
import pathlib
import re

try:
    from HostDict import MachineIPs
except ModuleNotFoundError:
    log.error("Please Run ProcessHosts.py File")


def _LEN(value):
    if value != None:
        return(len(value))
    else:
        return(0)


def green(text):
    return(f"\033[92m{text}\033[0m")


class Writeup():
    def __init__(self, Args, Client, Creds=False):
        self.Machine_ID = Args.machine
        self.Challenge_ID = Args.challenge
        self.Client = Client
        self.WriteupFolder = "C:\\Users\\Owner\\OneDrive\\Documents\\OneDrive\\Documents\\HTB Writeups\\WriteMeUp\\TimeToWriteUp\\"
        if Creds:
            Username, Password = Creds[:2]

        if os.name == "posix":
            self.Home = os.getenv("HOME")
        elif os.name == "nt":
            self.Home = os.getenv("%UserProfile%")

        if self.Machine_ID:
            log.info(f"Processing Machines : {green(self.Machine_ID)}")
            self.MachineWriteup()

        if self.Challenge_ID:
            log.info(f"Processing Challenges : {green(self.Challenge_ID)}")
            self.ChallengeWriteup()

        if not self.Challenge_ID and not self.Machine_ID:
            log.error("ID Argument Missing")

    def MachineWriteup(self):
        for number in self.Machine_ID:
            try:
                log.progress(f"Machine ID : {number}")
                MachineObj = self.Client.get_machine(number)
                File = f"{MachineObj.name}.md"
                File = re.sub(r'[^\w\-_\. ]', '_', File)
                Filename = self.WriteupFolder + f"Boxes\\_Headers\\{File}"

                try:
                    MachineIP = MachineIPs[str(number)]
                except KeyError:
                    log.error(
                        "Please Run Process Hosts.py with the -Refresh Flag")

                with open(Filename, "w+") as f:
                    Content = f"HTB - {MachineObj.name.title()} [{MachineObj.difficulty}]\n"
                    Content += f"**Name** : {MachineObj.name}\n"
                    Content += f"**Difficulty** : {MachineObj.difficulty}\n"
                    Content += f"**OS** : {MachineObj.os}\n"
                    Content += f'**URL** : [{"https://app.hackthebox.eu/machines/" + str(number)}]({"https://app.hackthebox.eu/machines/" + str(number)})\n'
                    Content += f"**Points** : {MachineObj.points}\n"
                    Content += f"**Stars** : {MachineObj.stars}\n"
                    Content += f"**Internal IP** : {MachineIP}\n"
                    f.write(Content)

                log.success(f"    Written to {File}\n")
            except errors.NotFoundException:
                log.info("Machine with this ID does not exist.\n")

    def ChallengeWriteup(self):
        for number in self.Challenge_ID:
            try:
                log.progress(f"Challenge ID : {number}")
                ChallengeObj = self.Client.get_challenge(number)

                File = f"{ChallengeObj.name}.md"
                File = re.sub(r'[^\w\-_\. ]', '_', File)
                Filename = self.WriteupFolder + f'Challenges\\_Headers\\{File}'

                with open(Filename, "a+", encoding='utf-8') as f:
                    Content = f"HTB - {ChallengeObj.name.title()} [{ChallengeObj.category}]\n\n"
                    Content += f"```\n**Name** : {ChallengeObj.name}\n"
                    Content += f"**Category** : {ChallengeObj.category}\n"
                    Content += f"**Difficulty** : {ChallengeObj.difficulty}\n"
                    Content += f"**Description** : `{ChallengeObj.description}`\n"
                    Content += f'**URL** : [{"https://app.hackthebox.eu/challenge/" + str(number)}]({"https://app.hackthebox.eu/challenge/" + str(number)})\n'
                    Content += f"**Points** : {ChallengeObj.points}\n```"
                    f.write(Content)

                log.success(f"    Written to {File}")
            except errors.NotFoundException:
                log.info("Challenge with this ID does not exist.")


# Argparse
Parser = argparse.ArgumentParser()
Parser.add_argument("-challenge", "-c", metavar="", help="Use this to pass ChallengeIDs in order to generate the attached writeups",
                    action="store", nargs="*", default=None, type=int)
Parser.add_argument("-machine", "-m", metavar="", help="Use this to pass MachineIDs in order to generate the attached writeups",
                    action="store", nargs="*", default=None, type=int)
Args = Parser.parse_args()

if __name__ == "__main__":
    if ".creds" in os.listdir(os.getcwd()):
        log.info("".ljust(70, "="))
        log.progress("Processing .creds file")
        Email, Password = open(".creds").read().split("\n")[:2]
        log.progress("    Email in .creds file ".ljust(28) + ": " + Email)
        log.progress("    Password in .creds file ".ljust(
            28) + ": " + len(Password) * '*' + "\n")
        log.info("".ljust(70, "="))

    else:
        Email = str(input("\033[93mEnter your Email > \033[0m"))
        Password = getpass(f"\033[93mInput your Password > \033[0m")

    Client = HTBClient(email=Email, password=Password)
    log.success(f"Authenticated as {green(Client.user.name)}")
    c, m = _LEN(Args.challenge), _LEN(Args.machine)
    log.info(f"Processing {green(c)} Challenges and {green(m)} Machines")
    log.info("".ljust(70, "="))

    Writeup(Args, Client)
