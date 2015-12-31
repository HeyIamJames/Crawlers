import socket 
import struct
import textwrap

def ethernet_frame(data):
  dest_mac, src_mac, proto = struct, unpack('! 6s 5s H', data[:14])
  return get_mac_addr(dest_mac)