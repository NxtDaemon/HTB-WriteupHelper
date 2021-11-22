import os
import sys
import requests

Machine_IPs = {}

if len(sys.argv) > 1:
    if sys.argv[1].lower() == "-refresh":
        if "hosts.txt" in os.listdir(os.getcwd()):
            print("Deleting Hosts.txt")
            os.remove(os.path.join(os.getcwd(), "hosts.txt"))
        with open("hosts.txt", "w") as f:
            Content = requests.get(
                "https://raw.githubusercontent.com/fx2301/htb_etc_hosts/master/hosts.txt")
            print("Populating hosts.txt")
            f.write(Content.text)

if "hosts.txt" in os.listdir(os.getcwd()):
    with open("hosts.txt", "r") as f:
        Lines = f.readlines()
        for Line in Lines:
            Line = Line.strip()
            if len(Line.split("/")) != 1 and Line[-8:] != "machines" and "===" not in Line:
                Machine_IPs.update({Line.split("/")[-1].strip(): Line[:12]})

    with open("HostDict.py", "+w") as f:
        f.write(f"MachineIPs = {Machine_IPs}")

    print("Finish Formatting HostDict.py")
else:
    print("hosts.txt File Missing, please use the -Refresh flag")
