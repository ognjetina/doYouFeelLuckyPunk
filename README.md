DO YOU FEELE LUCKY PUNK
=========================
Do you feel lucky punk is a small web app written in pure Python for learning purposes.

App is starting server on hosts ip address with port 1337.
You can get json response if you visit /json.

App is simply scaning our local network and searching for our playstation 3 mac address,if the mac address is not present on network we assume that no one is playing ps3.

And yes I know that the app wont be telling the truth if some one leaves ps3 turned on but that's a human error.
Installation
-----------
Clone the app

run:
```
git clone https://github.com/ognjetina/doYouFeelLuckyPunk.git
```
App uses apr-scan

run:
```
sudo apt-get install arp-scan
```
clone project get inside of project and run:
```
sudo pip install -r requirements.txt
```

start the app:
```
sudo python do_you_feel_lucky_punk.py
```
since the app is using arpscan you need to start it as sudo.

