import subprocess



def get_everyone():
    batcmd = "sudo arp-scan -l"
    return subprocess.check_output(batcmd, shell=True)

def find_ps3(ps3_mac_address):
    if ps3_mac_address in get_everyone(): return True
