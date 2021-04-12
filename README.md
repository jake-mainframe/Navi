/* SOCKS5 REXX PROXY */  
Start Socks Proxy on 172.16.9.10 IP and Port 1080, No Auth  
/* ex 'jake.rexx(navisock)' '172.16.9.10 1080'*/  
Start Socks Proxy on 172.16.9.10 IP and Port 1080, User Pass Auth  
/* ex 'jake.navisock' '172.16.9.10 1080 JAKE PASS'*/  

Implemented most from this:  
https://tools.ietf.org/html/rfc1928  

Missing:  
/* TODO BIND Proxy */  
/* TODO other auth */  

Have Not Tested:   
/* TODO test IPV6 */  

End Program by sending a Newline with nc  


Use Proxy chains to make clients Socks 5 Compliant  
[ProxyList]
# add proxy here ...
# meanwile
# defaults set to "tor"
socks5 172.16.9.10 1080

mainframe@ubuntu:~$ proxychains curl -k http://172.16.0.54:8000  
ProxyChains-3.1 (http://proxychains.sf.net)  
|S-chain|-<>-172.16.9.10:1080-<><>-172.16.0.54:8000-<><>-OK  

Two Python programs have been included to test TCP and UDP  

