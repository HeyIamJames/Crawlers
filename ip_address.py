import os
from socket import gethostbyname

def get_ip_address(url):
    return gethostbyname(url)

def get_ip_address2(url):
    command = "host " + url
    #init new process
    process = os.popen(command)
    results = str(process.read())
    marker = results.find('has address') + 12
    #sice string pre ip
    return results[marker:].splitlines()[0]

print(get_ip_address2('google.com'))