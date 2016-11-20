DO YOU FEEL LUCKY PUNK
=========================
Do you feel lucky punk is a small web app written in pure Python for learning purposes.

App is starting server on hosts ip address with port.
You can get json response if you visit /json.

App is simply scanning our local network and searching for our playstation 3 mac address,if the mac address is not present on network we assume that no one is playing ps3.

And yes I know that the app wont be telling the truth if some one leaves ps3 turned on but that's a human error.
Installation
-----------
Clone the app

run:

App uses apr-scan so install it

run:
```
sudo apt-get install arp-scan
```

Get inside of project and run:
```
sudo pip install -r requirements.txt
```

Start the app:
since the app is using arpscan you need to start it as sudo.
```
sudo python manage.py runserver
```


