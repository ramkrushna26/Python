#!/usr/bin/python3

import scapy.all as scapy
import argparse

def getArgs():
	parser = argparse.ArgumentParser()
	parser.add_argument("-t", "--target", dest="target", help="Target IP/IP Range")
	option = parser.parse_args()
	return option


def scan(ip):
	# scapy.arping(ip)
	# scapy.ls(scapy.ARP)
	# scapy.ls(scapy.Ether())

	arpRequest = scapy.ARP(pdst=ip)
	# print(arpRequest.summary())
	# arpRequest.show()
	
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	# print(broadcast.summary())
	# broadcast.show()

	arpRequestBroadcast = broadcast/arpRequest
	# print(arpRequestBroadcast.summary())
	# arpRequestBroadcast.show()

	answered = scapy.srp(arpRequestBroadcast, timeout=1, verbose=False)[0]
	# print(answered.summary())
	
	clientList = []
	for item in answered:
		clientDict = {"IP": item[1].psrc, "MAC": item[1].hwsrc}
		clientList.append(clientDict)
	return clientList


def printClients(clientList):
	print("IP\t\t\tMAC Address\n-----------------------------------------")
	for client in clientList:
		print(client["IP"] + "\t\t" + client["MAC"])

option = getArgs()
scannedResult = scan(option.target)
printClients(scannedResult)