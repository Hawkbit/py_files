#conditionals and selection, using the networking code above
import socket
socket.setdefaulttimeout(10)
s = socket.socket()
s.connect(("ftp.adobe.com",21))
ans = s.recv(1024)
banner = "FreeFloat FTP Server"
if ("FreeFloat FTP Server (Version 1.00)" in ans):
    print "[+] FreeFloat FTP Server is vulnerable."
elif ("3Com 3CDaemon FTP Server Version 2.0" in banner):
    print "[+] 3CDaemon FTP Server is vulnerable."
elif ("Sami FTP Server 2.0.2" in banner):
    print "[+] Sami FTP Server is vulnerable."
elif ("220 Welcome to Adobe FTP services" in ans):
    print "[+] Adobe FTP Server is vulnerable."
else:
    print "[-] FTP Server is not vulnerable."
