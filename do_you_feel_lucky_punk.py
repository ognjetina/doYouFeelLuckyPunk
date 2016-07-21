import textwrap
import random
import datetime
import json
from six.moves.BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from scan_network import findPs3


def randomFreePSMessage():
    messages = [
        "Great news ps3 is free",
        "Dammn you are lucky ps3 is free!",
        "RUN RUN MAN ps3 is free!"
    ]
    return messages[random.randrange(0, 2)]


def randomTakenPSMessage():
    messages = [
        "Dammn some one is eather playing or left ps3 on...",
        "No luck mate!!! PS is taken"
    ]
    return messages[random.randrange(0, 1)]


def checkForPs3():
    isItTaken = findPs3("70:9e:29:3f:f1:67")
    changeCss = ['''color: green;''', '''color: red;''']

    if (isItTaken):
        message = randomTakenPSMessage()
        colorCss = changeCss[1]
    else:
        message = randomFreePSMessage()
        colorCss = changeCss[0]

    return message, colorCss, datetime.datetime.now().strftime("%Y-%m-%d %H:%M")


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path == '/json':
            message, colorCss, lastCheck = checkForPs3()
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response_text = {
                'message': message,
                'lastCheck': lastCheck
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
            message, colorCss, lastCheck = checkForPs3()
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
            <h2>Last time someone checked: ''' + lastCheck + '''</h2>
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
