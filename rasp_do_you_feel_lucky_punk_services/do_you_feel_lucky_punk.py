import random
from rasp_do_you_feel_lucky_punk_services.scan_network import is_device_on_network


def random_free_message():
    messages = [
        "Great news PS3 is free",
        "You are lucky PS3 is free!",
        "PS3 is free!"
    ]
    return messages[random.randrange(0, 2)]


def random_taken_message():
    messages = [
        "Sorry someone is either playing or left PS3 on.",
        "Sorry no luck mate!!! PS3 is taken.",
        "Sorry PS3 is taken."
    ]
    return messages[random.randrange(0, 2)]


def check_is_ps3_on_network():
    if (is_device_on_network("70:9e:29:3f:f1:67")):
        message = random_taken_message()
    else:
        message = random_free_message()

    return message
