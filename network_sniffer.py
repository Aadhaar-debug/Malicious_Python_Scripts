# Made by aadhaar Koul
# email - aadhaarkoul2002@gmail.com


# this program is designed to verbose all the traffic 
# that is existing in the current network

# we wil be using the scapy module to amke a network sniffer

import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)


scan("10.0.2.1/24")