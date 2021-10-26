from hackthebox import *
from getpass import getpass
from pwn import *
import argparse
import os


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
        self.Home = os.getenv("HOME")  # * for Windows use "%UserProfile%"

        if self.Machine_ID:
            self.MachineWriteup()

        if self.Challenge_ID:
            self.Challenge()

        else:
            log.Error("ID Argument Missing")

    def MachineWriteup(self):
        for number in self.Machine_ID:
            try:
                log.progress(f"Machine ID : {number}")
                MachineObj = self.Client.get_machine(number)
                Filename = f"D:\\HTB\\{number}.md"

                if number <= 3:
                    MachineIP = "10.10.10." + str(number)
                else:
                    MachineIP = "10.10.10." + \
                        str(number - 3)  # ! May Need Fixing

                with open(Filename, "w+") as f:
                    f.write(f"""HTB - {MachineObj.name.capitalize()} [{MachineObj.difficulty}]\n\n**Name** : {MachineObj.name}\n**Difficulty** : {MachineObj.difficulty}\n**OS** : {MachineObj.os}**URL** : [{"https://app.hackthebox.eu/machines/" + str(number)}]({"https://app.hackthebox.eu/machines/" + str(self.Machine_ID)})\n**Points** : {MachineObj.points}\n**Stars** : {MachineObj.stars}\n**Internal IP** : 10.10.10.{MachineIP}""")

                log.progress(f"    Written to {Filename}\n")
            except errors.NotFoundException:
                log.info("Machine with this ID does not exist.\n")

    def Challenge(self):
        for number in self.Challenge_ID:
            try:
                log.progress(f"Challenge ID : {number}")
                ChallengeObj = self.Client.get_challenge(number)

                Filename = f"D:\\HTB\\{ChallengeObj.name}.md"
                with open(Filename, "a+") as f:
                    f.write(f"""HTB - {ChallengeObj.name.capitalize()} [{ChallengeObj.category}]\n\n**Name** : {ChallengeObj.name}\n**Category** : {ChallengeObj.category}\n**Difficulty** : {ChallengeObj.difficulty}**Description** : `{ChallengeObj.description}`\n**URL** : [{"https://app.hackthebox.eu/challenge/" + str(number)}]({"https://app.hackthebox.eu/challenge/" + str(self.Challenge_ID)})\n**Points** : {ChallengeObj.points}""")

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
    Password = getpass(f"\033[93mInput your Password > \033[0m")
    Client = HTBClient(email="", password=Password)
    print(f"[*] Authenticated as {green(Client.user.name)}")
    c, m = _LEN(Args.challenge), _LEN(Args.machine)
    print(f"[*] Processing {green(c)} Challenges and {green(m)} Machines")
    Writeup(Args, Client)
