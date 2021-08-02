# google translate tts

import base64
import requests
import urllib.parse
from tkinter import *
import tkinter.messagebox

class Main_GUI():
	def __init__(self,window):
		self.window = window

	def set_window_ui(self):
		self.window.title('Google娘语音生成器')	# ui标题
		self.window.geometry('450x150+700+350')	# ui坐标，*x*（长宽）；+*+*（屏幕显示位置）
		self.window.attributes('-alpha',0.9)	# 窗口属性，alpha是透明度，后面的小数是透明度设置（0-1）
		# grid方法:
		# row 行号：
		# column：列号
		# rowspan：合并一列中的多个行单元
		# columnspan：合并一个行中的多个列单元
		# sticky：NSWE，上下左右对齐，左右居中则：E+W；上下居中则：N+S；全居中则：N+S+E+W
		self.text_label_fill0 = Label(self.window, text='', width=1).grid(row=0, column=0)# 美化填充列
		self.text_label_fill0 = Label(self.window, text='语音文字：').grid(row=0, column=1, sticky=E)
		self.enter_text = Text(self.window, width=60, height=5)# 文本输出框
		self.enter_text.grid(row=1, column=1, columnspan=7)# 格式在当前版本的库中必须换行，不然会报错
		self.text_label1 = Label(self.window, text='输出文件名：', height=2).grid(row=2, column=1, sticky=E)
		self.filename_entry = Entry(self.window)# 输入框
		self.filename_entry.grid(row=2,column=3)# 格式在当前版本的库中必须换行，不然会报错
		self.check_button1 = Button(self.window, text='生成', command=self.Output).grid(row=2, column=5)
		self.check_button2 = Button(self.window, text='关于', command=self.Message).grid(row=2, column=7)


	# 语音输出函数
	def Output(self):
		gt_url = 'https://translate.google.cn/_/TranslateWebserverUi/data/batchexecute'
		headers = {'Content-Type':'application/x-www-form-urlencoded;charset=utf-8'}
		text = self.enter_text.get('0.0','end').replace('\n', '')
		req = "[[[\"jQ1olc\",\"[\\\""+text+"\\\",\\\"zh-CN\\\",true]\",null,\"generic\"]]]"
		req = urllib.parse.quote(req.encode("utf-8"))
		data = "f.req="+req
		r = requests.post(url=gt_url,data=data,headers=headers)
		tts_encode = r.text.split(',')[2][4:-4]
		tts = base64.b64decode(tts_encode)

		name = self.filename_entry.get()

		if len(name) ==0:
			filename ='output.mp3'
		elif 'mp3' in name:
			filename = name
		else:
			filename = name +'.mp3'

		with open(filename,"wb") as f:
			f.write(tts)

		tkinter.messagebox.showinfo('：)','语音文件：'+filename+' 生成完成!')

	# 弹窗函数
	def Message(self):
		tkinter.messagebox.showinfo('Google娘语音生成器 by alee','这是一个调用Google翻译api的小程序。\n\n可以将输入内容对应的朗读下载到当前目录!')


if __name__ == '__main__':
	window = Tk()
	GUI_HOME = Main_GUI(window)
	GUI_HOME.set_window_ui()
	window.mainloop()



