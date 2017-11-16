import crypt # this is only available in the Linux version on python

# testPass - takes encrypted password as parameter and returns
# 1. after finding password
# 2. after exhausting words in dictionary

def testPass(cryptPass):
    salt = cryptPass[0:2] # strips first two values of password
    dictfile = open('dictionary.txt', 'r')
    for word in dictfile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        if (cryptWord == cryptPass):
            print "[+] Found password: " + word + "\n"
            return
