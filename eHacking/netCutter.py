
import netfilterqueue
import scapy.all as scapy

def processPacket(packet):
	scapyPacket = scapy.IP(packet.get_payload())
	print(scapyPacket.show())
	packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, processPacket)
queue.run()