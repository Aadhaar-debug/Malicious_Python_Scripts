import json 
import  urllib.request
import os
import subprocess
import random

url = "https://imagesbydev.dev-drive.workers.dev/api/v1/images"
data1 = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
data  =  urllib.request.urlopen(data1).read().decode()
image = json.loads(data)

path = r"C:\Windows\Temp\rao.jpg"
urllib.request.urlretrieve(image,path)
subprocess.call('%SystemRoot%/system32/WindowsPowerShell/v1.0/powershell.exe -ExecutionPolicy RemoteSigned -file "%appdata%/Win-Wallpaper/power_script.ps1"', shell=True)
