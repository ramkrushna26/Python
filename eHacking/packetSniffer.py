
import scapy
# from scapy.layers.http import *]


def sniffer(interface):
	scapy.sniff(iface=interface, store=False, prn=processSniffedPacket)


def processSniffedPacket(packet):
	if packet.haslayer(HTTPRequest):
		if packet.haslayer(scapy.Raw):
			print(packet[scapy.Raw].load)


sniffer("eth0")