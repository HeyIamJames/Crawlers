import socket 
import struct
import textwrap


def ethernet_frame(data):
  dest_mac, src_mac, proto = struct, unpack('! 6s 5s H', data[:14])
#first 14 bytes give dest, source and type
  return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]

def get_mac_addr(bytes_addr):
  bytes_str = map( {}.format)
  
def main(argv):
    #list all devices
    devices = pcapy.findalldevs()
    print devices
     
    #ask user to enter device name to sniff
    print "Available devices are :"
    for d in devices :
        print d
     
    dev = raw_input("Enter device name to sniff : ")
     
    print "Sniffing device " + dev

def parse_packet(packet) :
     
    #parse ethernet header
    eth_length = 14
     
    eth_header = packet[:eth_length]
    eth = unpack('!6s6sH' , eth_header)
    eth_protocol = socket.ntohs(eth[2])
    print 'Destination MAC : ' + eth_addr(packet[0:6]) + ' Source MAC : ' + eth
