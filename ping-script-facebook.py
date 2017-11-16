import os
import time
i=0
hostname = "facebook.com" #example

while (i<100):
    response = os.system("ping -c 1 " + hostname)
    #and then check the response...
    if response == 0:
      testToAppend = hostname+ ' is up!'
    else:
      testToAppend = hostname+ ' is down!'
    
    with open("facebook.txt", "a") as myfile:
      myfile.write(testToAppend)
      myfile.write("\n")
    #Pause 1 sec
    time.sleep(1)