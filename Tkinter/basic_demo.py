from tkinter import *
import tkinter.messagebox

class Main_GUI():
	def __init__(self,window):
		self.window = window

	def set_window_ui(self):
		self.window.title('basic demo 小工具 by alee')	# ui标题
		self.window.geometry('600x400+700+350')	# ui坐标，*x*（长宽）；+*+*（屏幕显示位置）
		self.window.attributes('-alpha',0.9)	# 窗口属性，alpha是透明度，后面的小数是透明度设置（0-1）
		# grid方法:
		# row 行号：
		# column：列号
		# rowspan：合并一列中的多个行单元
		# columnspan：合并一个行中的多个列单元
		# sticky：NSWE，上下左右对齐，左右居中则：E+W；上下居中则：N+S；全居中则：N+S+E+W
		self.text_label_fill0 = Label(self.window, text='', width=1).grid(row=0, column=0)# 美化填充列
		self.text_label1 = Label(self.window, text='input：',width=7, height=2).grid(row=0, column=1, sticky=E)# 显示文本
		self.text_label_fill1 = Label(self.window, text='', width=1).grid(row=0, column=2)# 美化填充列
		self.ip_addr_entry = Entry(self.window)# 输入框
		self.ip_addr_entry.grid(row=0,column=3)# 格式在当前版本的库中必须换行，不然会报错
		self.text_label_fill2 = Label(self.window, text='', width=1).grid(row=0, column=4)# 美化填充列
		self.check_button1 = Button(self.window, text='output', command=self.Output).grid(row=0, column=5)
		self.text_label_fill3 = Label(self.window, text='', width=1).grid(row=0, column=6)# 美化填充列
		self.check_button2 = Button(self.window, text='message', command=self.Message).grid(row=0, column=7)
		self.result_text = Text(self.window, width=60, height=20)# 文本输出框
		self.result_text.grid(row=1, column=1, columnspan=7)# 格式在当前版本的库中必须换行，不然会报错

	# 文本显示函数
	def Output(self):
		entry_data = self.ip_addr_entry.get()+'\n'
		self.result_text.insert(END,entry_data)

	# 弹窗函数
	def Message(self):
		tkinter.messagebox.showinfo('hi','This is a Demo Tool!')

if __name__ == '__main__':
	window = Tk()
	GUI_HOME = Main_GUI(window)
	GUI_HOME.set_window_ui()
	window.mainloop()
