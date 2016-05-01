from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor
import os
SERVER_HOST="localhost"
SERVER_PORT=8008

class ClientConnection(Protocol):
	def __init__(self,address):
		self.addr = address
	def connectionMade(self):
		print "new connection made to "+SERVER_HOST+" port "+str(SERVER_PORT)
		self.transport.write("GET /movies/32 HTTP/1.0\r\n\r\n") #When the connection is made issue a get request to the server: student02.cse.nd.edu
		self.transport.loseConnection()
	def dataReceived(self,data):
		print "recieved data: "+ data
	def connectionLost(self,reason):
		print "lost connection to "+SERVER_HOST+" port "+str(SERVER_PORT)
		os._exit(1)
class ClientConFactory(ClientFactory):
	def buildProtocol(self, addr):
		return ClientConnection(addr)
	def doStart(self):#do start do bop a bop bop de bop
		pass
	def startedConnecting(self,addr):
		pass
	def clientConnectionFailed(self,addr,reason):
		pass
	def doStop(self):#do stop a dop de bop bop de wop 
		pass 

if __name__ == "__main__":
	reactor.connectTCP(SERVER_HOST,SERVER_PORT,ClientConFactory()) # Set up a tcp connection with the server and create connections using client connection factory.
	reactor.run()#Start the event loop which responds to server connections
