import os

Machine_IPs = {}

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
    print("hosts.txt File Missing, please pull it from the github repo")
