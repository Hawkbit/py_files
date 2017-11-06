#networking w/ python and socket
import socket
socket.setdefaulttimeout(10)
s = socket.socket()
s.connect(("193.104.215.67",21)) #"192.168.95.148" from book, but appears dead server
# 193.104.215.67 is ftp.adobe.com
ans = s.recv(1024) #reads first 1024 bytes on socket
print ans
