# import sys
import os
from api import Api

if not os.path.exists("config.txt"):
	print("config.txt文件缺失")
	os.system("pause")
	exit(0)
a = open("config.txt","r").readlines()
proxies = None if a[0].split("=")[1].strip() == "None" else a[0].split("=")[1].strip()
specificID = None if a[1].split("=")[1].strip() == "None" else a[1].split("=")[1].strip()

if __name__ == '__main__':
	# if len(sys.argv) != 1 
	# print(sys.argv)
	Api(proxies=proxies,specificID=specificID).start()
