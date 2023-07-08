# import sys
import os
from api import Api
from geetest import dealCode

if not os.path.exists("config.txt"):
	print("config.txt文件缺失")
	os.system("pause")
	exit(0)

a = open("config.txt","r").readlines()
proxies = None if a[0].split("=")[1].strip() == "None" else a[0].split("=")[1].strip()
specificID = None if a[1].split("=")[1].strip() == "None" else a[1].split("=")[1].strip()
sleep = eval(a[2].split("=")[1].strip())

if __name__ == '__main__':
	if not os.path.exists("url"):
		with open("url","w") as f:
			f.write("")
	Api(proxies=proxies,specificID=specificID,sleepTime=sleep,).start()
