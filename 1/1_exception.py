# exception handling
try:
    print "[+] 1337/0 = " + str(1337/0)
except Exception, e:
    print "[-] Error = " + str(e)
