from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol
from twisted.protocols.basic import LineReceiver
from twisted.internet.tcp import Port
from twisted.internet import reactor
import SpaceInvaders
import os
MY_PORT = 40015

class MyConnection(Protocol):
	
	def __init__(self,addr):
		self.addr = addr
		#self.delimeter = "|"
	def connectionMade(self):
		print "connection received from "+ str(self.addr)
	def connectionLost(self,reason):
		print "connection lost from "+str(self.addr)
		os._exit(1)
#		reactor.stop()
	def dataReceived(self, line):
		print "data received: "+line

class MyConnFactory(Factory):
	
	def buildProtocol(self,addr):
		return MyConnection(addr)

if __name__=="__main__":
	reactor.listenTCP(MY_PORT,MyConnFactory())
	reactor.run()
	sys.exit()
