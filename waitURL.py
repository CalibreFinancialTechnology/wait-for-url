import os
import requests
import sys
import time

timeSoFar = 0
waitTime = 5

# Arg 1 : URL
# Arg 2 : timeout
# Arg 3 : command

url = sys.argv[1]
timeOut = int(sys.argv[2])
command = sys.argv[3:]

print("Attempting to connect to URL: %s and then run command %s" % (url, command))

while True and timeSoFar < timeOut:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Connected to URL %s" % url)
            os.system(" ".join(command))
            break
        else:
            print("URL %s not available with status code of %s" % (url, response.status_code))
            timeSoFar = timeSoFar + waitTime
            time.sleep(waitTime)

    except:
        e = sys.exc_info()[0]
        print("Unable to connect to URL %s due to: %s" % (url, e))
        timeSoFar = timeSoFar + waitTime
        time.sleep(waitTime)

print("waitURL completed for %s " % url)
