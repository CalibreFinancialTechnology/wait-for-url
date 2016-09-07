#!/usr/bin/env python

import os
import sys
import time
import urllib2

timeSoFar = 0
waitTime = 5

# Arg 1 : URL
# Arg 2 : timeout
# Arg 3 : command

url = sys.argv[1]
timeOut = int(sys.argv[2])
command = sys.argv[3:]

print("Attempting to connect to URL: %s and then run command %s" % (url, command))

req = urllib2.Request(url)

while timeSoFar < timeOut:
    try:
        res = urllib2.urlopen(req)
	if res.code == 200:
	    print("Connected to URL %s" % url)
            os.system(" ".join(command))
            break
        else:
            timeSoFar = timeSoFar + waitTime
            time.sleep(waitTime)

    except (urllib2.HTTPError, urllib2.URLError):
        timeSoFar = timeSoFar + waitTime
        time.sleep(waitTime)

        
print("waitURL completed for %s " % url)
