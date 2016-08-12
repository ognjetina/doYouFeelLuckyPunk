import textwrap
import random
import datetime
import json
from six.moves.BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from scan_network import *


def random_free_message():
    messages = [
        "...great news PS3 is free",
        "...you are lucky PS3 is free!",
        "...PS3 is free!"
    ]
    return messages[random.randrange(0, 2)]


def random_taken_message():
    messages = [
        "...someone is either playing or left PS3 on.",
        "...no luck mate!!! PS3 is taken.",
        "...PS3 is taken."
    ]
    return messages[random.randrange(0, 2)]


def check_for_ps3():
    isItTaken = find_ps3("70:9e:29:3f:f1:67")
    changeCss = ['''color: green;''', '''color: red;''']

    if (isItTaken):
        message = random_taken_message()
        colorCss = changeCss[1]
    else:
        message = random_free_message()
        colorCss = changeCss[0]

    return message, colorCss


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path == '/json':
            message, colorCss = check_for_ps3()
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response_text = {
                'message': message
            }
            self.wfile.write(json.dumps(response_text))

        elif self.path == '/about':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            response_text = textwrap.dedent('''
            <html>
            <head>
            <title>do you feel lucky punk</title>
            </head>
            <body>
            <div id="about">
            <hr>
            <p>Do you feel lucky punk is a small web app written in pure Python for learning purposes.</p>
            App is starting server on hosts ip address with port 1337. </br>
            You can get json response if you visit<a href="/json"> /json</a>.</br>
            App is simply scaning our local network and searching for our playstation 3 mac address,
            if the mac address is not present on network we assume that no one is playing ps3.</br>
            And yes I know that the app wont be telling the true if some one leaves ps3 turned on but that's a human error.
            </p>
            <hr>
            <p style="text-align:right;"><small>made by ognjetina</small></p>
            </div>
            <div style="text-align:center;">
            <a href="/"><p>back</p></a>
            </div>
            <style>
            p {
            text-align: justified;
            }
            #about {
            width: 50%;
            margin: 0 auto;
            }
            </style>''')
            self.wfile.write(response_text.encode('utf-8'))
        else:
            message, colorCss = check_for_ps3()
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            response_text = textwrap.dedent('''
            <html>
            <head>
            <title>do you feel lucky punk</title>
            </head>
            <body>
            <h1>''' + message + '''</h1>
            <a href="/about"><p>about</p></a>
            </body>
            </html>
            <style>
            h1 {
            text-align: center;
            ''' + colorCss + '''
            }
            h2 {
            text-align: center;
            }
            p{
            text-align: center;
            }
            </style>''')
            self.wfile.write(response_text.encode('utf-8'))


server_address = ('', 1337)
httpd = HTTPServer(server_address, RequestHandler)
print("Server is running.")
httpd.serve_forever()
