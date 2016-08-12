import subprocess
#using subprocess to spawn new proces that is sending
# arp-scan -l command on terminal and gets output of that
#process.

def get_everyone():
    batcmd = "sudo arp-scan -l"
    return subprocess.check_output(batcmd, shell=True)


def find_ps3(ps3_mac_address):
    if ps3_mac_address in get_everyone(): return True
