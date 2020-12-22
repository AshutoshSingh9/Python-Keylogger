import socket
import os
import requests
import sys
import urllib
import time
from datetime import datetime
from urllib import request as urlrequests
 
def logger():
    s = socket.socket()
    windows_ip = input("Enter address: ")
 
    try:
        host = windows_ip
        port = 80
 
        s.bind((host, 80))
    except:
        print("address is in use already")
        print("Use another address!")
 
    while True:
        try:
            s.listen(5)
            conn, address = s.accept()
 
            print("[+] IP Logged " + str(address[0]))
 
        except:
            pass
            print("Exiting...")
            sys.exit(0)
 
 
logger()