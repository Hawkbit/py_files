#variables and types
port = 21 #int
print type(port)
banner = "FreeFloat FTP Server" #string
print type(banner)
portList = [21,22,80,110] #list
print type(portList)
portOpen = True #boolean
print type(portOpen)

#concatenate
print "[+] Checking for " + banner + " on port " + str(port)

#string functions
print banner.upper()
print banner.lower()
print banner.replace('FreeFloat', 'Ability')
print banner.find('FTP')

#list functions
portList = []
portList.append(21)
portList.append(80)
portList.append(443)
portList.append(25)
print portList
portList.sort()
print portList
pos = portList.index(80)
print "[+] There are "+str(pos)+" ports to scan before port "+str(portList[2])+"."
portList.remove(443)
print portList
cnt = len(portList)
print "[+] Scanning "+str(cnt)+" Total ports."

#dictionaries
services = {'ftp':21,'ssh':22,'smtp':25,'http':80}
print services.keys()
print services.items()
print services.has_key('ftp')
print services['ftp']
print "[+] Found vuln with FTP on port "+str(services['ftp'])

#networking w/ python and socket
import socket
socket.setdefaulttimeout(10)
s = socket.socket()
s.connect(("193.104.215.67",21)) #"192.168.95.148" from book, but appears dead server
# 193.104.215.67 is ftp.adobe.com
ans = s.recv(1024) #reads first 1024 bytes on socket
print ans

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

# exception handling
try:
    print "[+] 1337/0 = " + str(1337/0)
except Exception, e:
    print "[-] Error = " + str(e)

#functions
import socket
def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return
def checkVulns(banner):
    if 'FreeFloat Ftp Server (Version 1.00)' in banner:
        print '[+] FreeFloat FTP Server is vulnerable.'
    elif '3Com 3CDaemon FTP Server Version 2.0' in banner:
        print '[+] 3CDaemon FTP Server is vulnerable.'
    elif 'Ability Server 2.34' in banner:
        print '[+] Ability FTP Server is vulnerable.'
    elif 'Sami FTP Server 2.0.2' in banner:
        print '[+] Sami FTP Server is vulnerable.'
    else:
        print '[-] FTP Server is not vulnerable.'
    return
def main():
    ip1 = '192.168.95.148'
    ip2 = '192.168.95.149'
    ip3 = '192.168.95.150'
    port = 21
    banner1 = retBanner(ip1, port)
    if banner1:
        print '[+] ' + ip1 + ': ' + banner1.strip('\n')
        checkVulns(banner1)
    banner2 = retBanner(ip2, port)
    if banner2:
        print '[+] ' + ip2 + ': ' + banner2.strip('\n')
        checkVulns(banner2)
    banner3 = retBanner(ip3, port)
    if banner3:
        print '[+] ' + ip3 + ': ' + banner3.strip('\n')
        checkVulns(banner3)
if __name__ == '__main__':
    main()

#iteration
for x in range(1, 255):
    print "192.168.95."+str(x)

portList = [21,22,25,80,110]
for port in portList:
    print port

# sys module provides access to objects used by python interpreter
import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
    print "[+] Reading Vulnerabilities From: " + filename

#  os module provides OS routines for Mac, NT and Posix OSs.
import os
if len(sys.argv) == 2:
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print "[-] " + filename + " does not exist."
        exit(0)
    if not os.access(filename, os.R_OK):
        print "[-] " + filename + " access denied."
        exit(0)
    print "[+] Reading Vulnerabilities From: " + filename
