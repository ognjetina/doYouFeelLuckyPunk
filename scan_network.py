import subprocess


def getEveryone():
    batcmd = "sudo arp-scan -l"
    return subprocess.check_output(batcmd, shell=True)


def findPs3(ps3Mac):
    if ps3Mac in getEveryone(): return True
