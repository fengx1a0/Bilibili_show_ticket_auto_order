# import sys
import os
import sys

from api import Api, addr_dict
from geetest import dealCode

if not os.path.exists("config.txt"):
    print("config.txt文件缺失")
    os.system("pause")
    exit(0)

a = open("config.txt", "r").readlines()
proxies = None if a[0].split("=")[1].strip() == "None" else a[0].split("=")[1].strip()
specificID = None if a[1].split("=")[1].strip() == "None" else a[1].split("=")[1].strip()
sleep = eval(a[2].split("=")[1].strip())
token = None if a[3].split("=")[1].strip() == "None" else a[3].split("=")[1].strip()

if __name__ == '__main__':
    # 收货地址文件
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'address.txt')

    if not os.path.exists(file_path):
        print("缺少收件人地址信息文件address.txt，已生成")
        print("若需订购需要邮寄的票，请关闭程序，填写完后重新运行")
        with open(file_path, "w") as f:
            f.write("姓名：\n电话:\n地址id:\n地址：\n")
    else:
        print("存在收货地址")
        with open(file_path, 'r') as f:
            for line in f:
                key, value = line.strip().split("：")
                addr_dict[key] = value
    # print(addr_dict)
    if any(value == '' or value is None for value in addr_dict.values()):
        print("地址文件中有项目未填写，将不可订购需要邮寄的票")

    if not os.path.exists("url"):
        with open("url", "w") as f:
            f.write("")
    Api(proxies=proxies, specificID=specificID, sleepTime=sleep, token=token).start()
