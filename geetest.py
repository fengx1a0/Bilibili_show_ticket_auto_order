import os
import json
import win32api,win32con
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class dealCode():
	def __init__(self,specificID=None):

		self.specificID = specificID
		self.cookies = {}
		self.u = ""

	def load_cookies(self):
		if not os.path.exists("user_data.json"):
			print("未找到用户数据文件")
			os.system("pause")
			exit()
		with open("user_data.json","r") as r:
			try:
				data = json.load(r)
				if len(data) == 0:
					raise ""
			except:
				print("数据文件错误")
			if self.specificID:
				data = data[self.specificID][1]
			else:
				data = data[list(data.keys())[0]][1]
			for item in data.split(";"):
				i = item.split("=")
				if len(i) == 2:
					self.WebDriver.add_cookie(cookie_dict={"domain": ".bilibili.com" ,'name' : i[0].strip(), 'value' : i[1].strip()})
	
	def init_browser(self):
		options = webdriver.EdgeOptions()
		options.add_argument("--log-level=3")
		self.WebDriver = webdriver.Edge(options=options)
		self.WebDriver.get("https://bilibili.com")
		self.WebDriver.delete_all_cookies()

	def load_code(self,url):
		print("token需要验证！！正在加载验证码，请完成验证后关闭网页！！")
		self.init_browser()
		self.load_cookies()
		self.WebDriver.get(url)
		while True:
			sleep(0.1)
			try:
				self.WebDriver.execute_script('javascript:void(0);')
			except:
				return 1

	def test(self):
		self.load_code("https://bilibili.com")

	def send_notifycation (content,title,tip_type='None', duration=5):
	    """
	    【功能】模拟windows发系统通知
	    【参数】
	        content: str   必选,通知内容
	        title: str     可选,通知标题
	        tip_type: str  可选,通知类型[None|Info|Warning|Error]
	        duration: int  可选,停留时长,单位(秒)
	    【输入/输出】 None
	    """
	    d = {}
	    for c in (65, 97):
	        for i in range(26):
	            d[chr(i+c)] = chr((i+13) % 26 + c)
	    s = ''
	    s += "shapgvba Fraq-Abgvsvpngvba{cnenz ([Fgevat] $pbagrag='Abgvsvpngvbaf',"
	    s += "[Fgevat] $gvc_gvgyr='Arj abgvsvpngvba',[Fgevat] $gvc_glcr='Abar',"
	    s += "[Vag32] $qhengvba=3);cebprff{Nqq-Glcr -NffrzoylAnzr Flfgrz.Jvaqbjf"
	    s += ".Sbezf;$nffrzoyl='Flfgrz.Jvaqbjf.Sbezf.AbgvslVpba';$abgvsl=Arj-"
	    s += "Bowrpg $nffrzoyl -Cebcregl @{Vpba=[Flfgrz.Qenjvat.FlfgrzVpbaf]::"
	    s += "Vasbezngvba;OnyybbaGvcVpba=$gvc_glcr;OnyybbaGvcGvgyr=$gvc_gvgyr;"
	    s += "OnyybbaGvcGrkg=$pbagrag;Ivfvoyr=$gehr};$abgvsl.FubjOnyybbaGvc"
	    s += "($qhengvba)}};Fraq-Abgvsvpngvba -pbagrag '%f' -gvc_gvgyr '%f' "
	    s += "-gvc_glcr '%f' -qhengvba %f"
	    subprocess.Popen(["PowerShell", '-ep', 'Unrestricted', '-nop',
	                      '-win', 'Hidden', '-c', '& {%s}' % (
	                        "".join([d.get(c, c) for c in (s)]) % (
	                            content, title, tip_type, duration))
	                    ])

	def mult_work(self):
		self.init_browser()
		self.load_cookies()
		while True:
			sleep(0.25)
			a = open("url","r")
			u = a.read()
			a.close()
			if u and u != self.u:
				self.u = u
				win32api.MessageBox(0,'需要滑块验证！','通知',win32con.MB_OK)
				self.WebDriver.get(u)

if __name__ == '__main__':
	dealCode().mult_work()


