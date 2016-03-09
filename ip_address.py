import os

def get_ip_address(url):
    command = "host" + url
    #init new process
    process - os.open(command)
    results = str(process.read())
    marker = results.find('has address') + 12 
    #sice string pre ip
    return results[marker:].splitlines()[0]
