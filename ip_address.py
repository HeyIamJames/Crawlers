import os

def get_ip_address(url):
    command = "host " + url
    #init new process
    process = os.popen(command)
    results = str(process.read())
    marker = results.find('has address') + 12
    #sice string pre ip
    return results[marker:].splitlines()[0]

print(get_ip_address('google.com'))