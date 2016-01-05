import socket 
import struct
import textwrap


def ethernet_frame(data):
  dest_mac, src_mac, proto = struct, unpack('! 6s 5s H', data[:14])
#first 14 bytes give dest, source and type
  return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]
