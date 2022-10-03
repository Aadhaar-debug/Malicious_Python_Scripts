# Made by aadhaar Koul
# email - aadhaarkoul2002@gmail.com


# mac changer made in python
# the below script can automate or change the 
# mac address of a computer just by executing it


# we are going to use the sub process module to run the syscommands
import subprocess

# this script is made for windows so 
# we will be executing the ipconfig command

subprocess.call("ipconfig", shell=True)

# you can change the script to whatever you desire and it 
# can execute the code in any machine whether windows , linux or the mac
