from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import time

class Main_GUI():
	def __init__(self,window):
		self.window = window

	def set_window_ui(self):
		self.window.title('easy demo 小工具 by alee')
		self.window.geometry('500x500+700+350')
		self.window.attributes('-alpha',0.9)
		self.text_label_fill0 = Label(self.window, text='', width=1).grid(row=0, column=0)
		self.text_label1 = Label(self.window, text='model:', height=3).grid(row=0, column=1, sticky=W+E)
		self.cmb = ttk.Combobox(self.window, width=9)# 下拉菜单控件，需要先导入ttk库
		self.cmb['value'] = ('model0','model1','model2','model3')# 下拉菜单列表内容
		self.cmb.current(0)# 指定默认显示在下拉框中的内容
		self.cmb.grid(row=0, column=2, sticky=W)# 格式在当前版本的库中必须换行，不然会报错
		self.check_button1 = Button(self.window, text='message', command=self.Message).grid(row=0, column=3)
		self.result_text = Text(self.window, width=50, height=20)
		self.result_text.grid(row=1, column=1, columnspan=3)
		self.result_text.insert(END,banner)
		self.text_label2 = Label(self.window, text='command:', height=3).grid(row=2, column=1, sticky=W)
		self.command_entry = Entry(self.window, width=30)
		self.command_entry.grid(row=2,column=2)
		self.check_button2 = Button(self.window, text='run', command=self.Run, width=5).grid(row=2, column=3, sticky=W+E)

	def FuncA(self,cmd):
		entry_data = 'model:'+self.cmb.get()+'\nhi, your command is '+cmd+'\n'+'================================\n'
		self.result_text.insert(END,entry_data)


	def Run(self):
		cmd = self.command_entry.get()
		if cmd =='':
			cmd = 'Null'
		current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		begin_data = '['+current_time+']'+'command: '+cmd+'\n'
		self.result_text.insert(END,begin_data)
		prt_funca = self.FuncA(cmd)

	def Message(self):
		tkinter.messagebox.showinfo('hi','This is a Demo Tool!')

if __name__ == '__main__':
	banner = '''
================================
    .___                     
  __| _/____   _____   ____  
 / __ |/ __ \\ /     \\ /  _ \\ 
/ /_/ \\  ___/|  Y Y  (  <_> )
\\____ |\\___  >__|_|  /\\____/ 
     \\/    \\/      \\/        
================================
'''
	window = Tk()
	GUI_HOME = Main_GUI(window)
	GUI_HOME.set_window_ui()
	window.mainloop()
