import subprocess


def get_everyone_on_network():
    batcmd = "sudo arp-scan -l"
    return subprocess.check_output(batcmd, shell=True)


def is_device_on_network(device_mac_address):
    if device_mac_address in get_everyone_on_network(): return True
