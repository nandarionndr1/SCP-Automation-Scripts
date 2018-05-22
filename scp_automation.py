import pexpect
import sys

#automation of file copying from an RPI using Putty SCP or PSCP


try:
    child = pexpect.spawn("scp pi@192.168.0.12:path/to/FILE_TO_BE_COPIED /path/to/DESTINATION")
    i = child.expect(["password:", pexpect.EOF])

    if i==0: # send password                
        child.sendline("YOUR_PASSWORD")
        child.expect(pexpect.EOF)
    elif i==1: 
        print ("Got the key or connection timeout")
        pass

except Exception as e:
        print ("Oops Something went wrong buddy")
        print (e)
