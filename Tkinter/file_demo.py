from tkinter import *
from tkinter import filedialog
import tkinter.messagebox


class Main_GUI():
	def __init__(self,window):
		self.window = window

	def set_window_ui(self):
		self.window.title('file demo 小工具 by alee')
		self.window.geometry('470x80+700+350')
		self.window.attributes('-alpha',0.9)
		self.text_label_fill0 = Label(self.window, text='', width=1).grid(row=0, column=0)
		self.text_label1 = Label(self.window, text='filepath:', height=3).grid(row=0, column=1, sticky=W+E)
		self.filepath_entry = Entry(self.window, width=30)
		self.filepath_entry.grid(row=0, column=2)
		self.text_label_fill0 = Label(self.window, text='', width=1).grid(row=0, column=3)
		self.check_button1 = Button(self.window, text='open', command=self.OpenFile).grid(row=0, column=4)

	def OpenFile(self):
		self.file_path = filedialog.askopenfilename() # 获取本地文件路径，需要引入filedialog库
		self.filepath_entry.delete(0,END)
		self.filepath_entry.insert(END,self.file_path)

if __name__ == '__main__':
	window = Tk()
	GUI_HOME = Main_GUI(window)
	GUI_HOME.set_window_ui()
	window.mainloop()
