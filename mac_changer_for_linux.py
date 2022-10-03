# Made by aadhaar Koul
# email - aadhaarkoul2002@gmail.com


# mac changer made in python
# the below script can automate or change the 
# mac address of a computer just by executing it


# we are going to use the sub process module to run the syscommands
import subprocess

interface = "wlan0"
new_mac = str(input("Enter the new mac to set it as a new one : "))

# this script is made for linux so 
# we will be executing the ipconfig command

print("[+] Changing the mac address for " + interface + " to " + new_mac)

subprocess.call("ifconfig", shell=True)
subprocess.call("ifconfig " + interface + " down ", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)




# you can change the script to whatever you desire and it 
# can execute the code in linux or the mac
