import os

def get_nmap(options, ip):
    command = "nmap " + options + " " + ip
    process = os.popen(command)
    results = str(process.read())
    return results 
     
# min value 0x0000001e

print(get_namp('-F', 'ip'))
