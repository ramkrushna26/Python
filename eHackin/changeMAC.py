#!/usr/bin/python3

import subprocess
import optparse
import re


def getArgs():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="connType", help="Interface to change MAC address")
	parser.add_option("-m", "--mac", dest="newMAC", help="New MAC address")
	(options, arguments) = parser.parse_args()
	if not options.connType:
		parser.error("[-] Please specify an interface, use --help for more info")
	elif not options.newMAC:
		parser.error("[-] Please specify a new mac, use --help for more info")
	return options


def changeMAC(connType, newMAC):
	print("[+] Changing MAC for " +  connType + " to " + newMAC)

	subprocess.call(["ifconfig", connType, "down"])
	subprocess.call(["ifconfig", connType, "hw",  "ether", newMAC])
	subprocess.call(["ifconfig", connType, "up"])


def getCurrentMAC(connType):
	ifconfigOutput = str(subprocess.check_output(["ifconfig", connType]))

	searchMACResult = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfigOutput)
	if searchMACResult:
		return searchMACResult.group(0)
	else:
		print("[-] Could not find MAC address")


options = getArgs()
currentMAC = getCurrentMAC(options.connType)
print("[+] Current MAC : ", currentMAC)

changeMAC(options.connType, options.newMAC)
currentMAC = getCurrentMAC(options.connType)
if currentMAC == options.newMAC:
	print("[+] MAC address changed successfully to ", currentMAC)
else:
	print("[-] MAC address did not changed")