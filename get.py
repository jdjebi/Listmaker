# coding: utf-8

import os
import subprocess
import re

# on prépare la regex
regex = re.compile(r"(?P<received>\d+) received")

# la fonction qui assure le ping
def ping(hostname):
    p = subprocess.Popen(["ping", "-c1", "-w100", hostname], stdout=subprocess.PIPE).stdout.read()
    #help(p.decode)
    r = regex.search(p.decode(errors='ignore'))
    try:
        if(r.group("received") == "1"):
            print("L'adresse %s existe!" % hostname) 
    except:
        pass

# on boucle sur les adresses du réseau local
for i in range(254):
    hostname = "192.168.0.%i" % (i+1)
    ping(hostname)