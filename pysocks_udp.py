import socks
from socket import *

s = socks.socksocket(AF_INET, SOCK_DGRAM) # Same API as socket.socket in the standard lib


s.set_proxy(socks.SOCKS5, "172.16.9.10",1080) # SOCKS4 and SOCKS5 use port 1080 by default






s.bind(("",1080))
s.connect(("172.16.0.54", 1234))


# Can be treated identical to a regular socket object
s.send(bytes("TEST\n","utf8"))
s.close()


#print(s.recv(4096))