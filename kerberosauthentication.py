import os
import subprocess
import jwtTest
import log

FNULL = open(os.devnull, 'w')

def kcheck():
    try:
        output = subprocess.check_call("klist", shell=False, stdout=FNULL, stderr=subprocess.STDOUT,)
    except subprocess.CalledProcessError as e:
        output = 1

    return output

usr = raw_input("Please enter your Username: ")

o = subprocess.call(["kinit",  usr])

if o == 1:
    subprocess.call("kdestroy", stdout=FNULL)

cred = kcheck()

if cred == 0:
    print "You are authorized!"
    token = jwtTest.jwtEncode(usr, "testUser")
    print token
    log.login(usr,'You are logged in!')
if cred == 1:
    print "No Ticket. Please try again."
    log.login(usr, 'Login Failed')
