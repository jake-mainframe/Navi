import socks

s = socks.socksocket() # Same API as socket.socket in the standard lib

s.set_proxy(socks.SOCKS5, "zos.jake.net",1080) # SOCKS4 and SOCKS5 use port 1080 by default


# Can be treated identical to a regular socket object
#s.connect(("172.16.0.54", 8000))

s.bind(('172.16.0.54', 8000))



s.sendall(bytes("GET / HTTP/1.1\n","utf8"))
s.sendall(bytes("\n","utf8"))



print(s.recv(4096))