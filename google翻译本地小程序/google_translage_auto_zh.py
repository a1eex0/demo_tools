# google translate en-zh

import requests
import urllib.parse
import json
from tkinter import *
import tkinter.messagebox

class Main_GUI():
	def __init__(self,window):
		self.window = window

	def set_window_ui(self):
		self.window.title('google translate auto to zh-CN')	# ui标题
		self.window.geometry('450x310+700+350')	# ui坐标，*x*（长宽）；+*+*（屏幕显示位置）
		self.window.attributes('-alpha',0.9)	# 窗口属性，alpha是透明度，后面的小数是透明度设置（0-1）
		self.window.resizable(False,False)	# 禁用窗口放大缩小
		# grid方法:
		# row 行号：
		# column：列号
		# rowspan：合并一列中的多个行单元
		# columnspan：合并一个行中的多个列单元
		# sticky：NSWE，上下左右对齐，左右居中则：E+W；上下居中则：N+S；全居中则：N+S+E+W
		self.text_label_fill0 = Label(self.window, text='', width=1).grid(row=0, column=0)# 美化填充列
		self.text_label_fill1 = Label(self.window, text='', width=1).grid(row=0, column=1)# 美化填充列
		self.text_label_fill2 = Label(self.window, text='', width=1).grid(row=0, column=2)# 美化填充列
		self.text_label_fill3 = Label(self.window, text='', width=1).grid(row=0, column=3)# 美化填充列
		self.text_label_fill4 = Label(self.window, text='', width=1).grid(row=0, column=4)# 美化填充列
		self.text_label_fill5 = Label(self.window, text='', width=1).grid(row=0, column=5)# 美化填充列
		self.text_label_fill6 = Label(self.window, text='', width=1).grid(row=0, column=6)# 美化填充列
		self.entry_text = Text(self.window, width=60, height=10)# 输入框
		self.entry_text.grid(row=0,column=1, columnspan=6)# 格式在当前版本的库中必须换行，不然会报错
		self.check_button1 = Button(self.window, text='翻译', command=self.Translate).grid(row=1, column=2)
		self.check_button2 = Button(self.window, text='清空', command=self.Clear).grid(row=1, column=4)
		self.check_button2 = Button(self.window, text='关于', command=self.Message).grid(row=1, column=6)
		self.result_text = Text(self.window, width=60, height=10)# 文本输出框
		self.result_text.grid(row=2, column=1, columnspan=6)# 格式在当前版本的库中必须换行，不然会报错


	# 弹窗函数
	def Message(self):
		tkinter.messagebox.showinfo('google translate auto to zh-CN by alee','这是一个调用Google翻译API的小程序。\n\n只有一个功能：自动检测语言，并翻译成中文。\n\n目前仅支持单词和长句的翻译！')

	def Clear(self):
		self.entry_text.delete('1.0','end')
		self.result_text.delete('1.0','end')

	# 翻译函数
	def Translate(self):
		gt_url = 'https://translate.google.cn/_/TranslateWebserverUi/data/batchexecute'
		headers = {'Content-Type':'application/x-www-form-urlencoded;charset=utf-8'}

		text = self.entry_text.get('0.0','end').replace('\n', ' ').replace('\r', ' ')

		req = "[[[\"MkEWBc\",\"[[\\\""+text+"\\\",\\\"auto\\\",\\\"zh-CN\\\",true],[null]]\",null,\"generic\"]]]"
		req = urllib.parse.quote(req.encode("utf-8"))
		data = "f.req="+req
		r = requests.post(url=gt_url,data=data,headers=headers)
		# 格式化处理
		j_1 = json.loads(r.text[6:])[0]
		j_2 = json.loads(j_1[2])
		j_3 = j_2[1][0][0]
		j_4 = json.dumps(j_3,ensure_ascii=False).split('"')
		# 拼音
		py_data = j_4[1]
		self.result_text.delete('1.0','end')
		self.result_text.insert(END,'\n')
		self.result_text.insert(END,py_data)
		self.result_text.insert(END,'\n\n')
		# 中文
		zw_data = j_4[5]
		self.result_text.insert(END,zw_data)

if __name__ == '__main__':
	window = Tk()
	GUI_HOME = Main_GUI(window)
	GUI_HOME.set_window_ui()
	window.mainloop()
