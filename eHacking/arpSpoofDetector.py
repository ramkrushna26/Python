
import scapy.all as scapy


def sniffer(interface):
	scapy.sniff(iface=interface, store=False, prn=processSniffedPacket)

def getMAC(ip):
	arpRequest = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arpRequestBroadcast = broadcast/arpRequest

	answered = scapy.srp(arpRequestBroadcast, timeout=1, verbose=False)[0]
	print(answered.show())
	return answered[0][1].hwsrc

def processSniffedPacket(packet):
	if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
		try:
			originalMAC = getMAC(packet[scapy.ARP].psrc)
			responseMAC = getMAC(packet[scapy.ARP].hwsrc)

			if originalMAC != responseMAC:
				print("[+] You are under attack!!")
		except IndexError:
			pass

sniffer("eth0")