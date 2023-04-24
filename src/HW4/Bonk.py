from scapy.all import *

ip = input('[*] Enter target IP: ')
ip_pkt = IP(dst=ip)
dport = 80

# SYN
sport = random.randint(1024, 65535)
seq_next = 0
SYN = TCP(sport=sport, dport=dport, flags='S', seq=seq_next)

# SYN/ACK
SYNACK = sr1(ip_pkt/SYN)
ack_next = SYNACK.seq + 1

# ACK
seq_next += 1
ACK = TCP(sport=sport, dport=dport, flags='A', seq=seq_next, ack=ack_next)
print(send(ip_pkt/ACK))

# DATA
for i in range(1000):
    # TCP 패킷의 시퀀스 넘버를 1번으로 조작
    DATA = TCP(sport=sport, dport=dport, flags='PA', seq=1, ack=ack_next)
    send(ip_pkt/DATA/"XX")
