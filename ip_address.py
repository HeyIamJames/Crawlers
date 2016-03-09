import os

def get_ip_address(url):
    command = "host" + url
    #init new process
    