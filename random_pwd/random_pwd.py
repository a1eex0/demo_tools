import random,string
import tkinter as tk
from tkinter import ttk
# string.ascii_lowercase	所有小写：a-z
# string.ascii_uppercase	所有大写：A-Z
# string.ascii_letters		全部大小写：a-z+A-Z
# string.digits				所有单数：0-9
# string.punctuation		特殊字符：!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~总长32个，包含了回车符、空格符等
# string.printable			所有大小写，数字，特殊字符
# string.hexdigits			所有十六进制单数：0-F
# 建议采用随机生成密码时，用（string.ascii_letters+string.digits+'!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'）。

win = tk.Tk()   
# 窗口属性
win.title("Random PWD")  
win.geometry('265x220+500+300')
win.resizable(False,False)
# win.attributes('-alpha',0.9)

# 生成函数
def Running():
	text1.insert('end','keywords：'+key.get()+'\t'+ 'length:'+number_chosen.get()+'\n')
	dic = ''
	if chVar0.get():
		dic += string.digits
	if chVar1.get():
		dic += string.ascii_uppercase
	if chVar2.get():
		dic += string.ascii_lowercase
	if chVar3.get():
		dic += '!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
	i = "".join(random.sample(dic, int(number_chosen.get())))
	text1.insert('end',key.get()+i+'\n--------------------\n')

# 清空函数
def Clearnning():
	text1.delete('1.0','end')

# 一个label标签
ttk.Label(win, text="关键字").grid(column=0, row=0)

# 一个输入框
key = tk.StringVar()
key_entered = ttk.Entry(win, width=12, textvariable=key)
key_entered.grid(column=0, row=1)

# 创建按钮
action = ttk.Button(win, text="生成", command=Running)
action.grid(column=2, row=1)

action = ttk.Button(win, text="清空", command=Clearnning)
action.grid(column=2, row=3)

# 一个label标签
ttk.Label(win, text="长度").grid(column=1, row=0)
# 创建一个下拉框
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=4, textvariable=number, state='readonly')
number_chosen['values'] = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
number_chosen.grid(column=1, row=1)
number_chosen.current(7)

# 创建一些复选框
chVar0 = tk.IntVar()
check0 = tk.Checkbutton(win, text="数字", variable=chVar0)
check0.select()
check0.grid(column=0, row=2, sticky=tk.W)

chVar1 = tk.IntVar()
check1 = tk.Checkbutton(win, text="大写字母", variable=chVar1)
check1.select()
check1.grid(column=1, row=2, sticky=tk.W)

chVar2 = tk.IntVar()
check2 = tk.Checkbutton(win, text="小写字母", variable=chVar2)
check2.select()
check2.grid(column=1, row=3, sticky=tk.W)

chVar3 = tk.IntVar()
check3 = tk.Checkbutton(win, text="特殊符号", variable=chVar3)
check3.select()
check3.grid(column=0, row=3, sticky=tk.W)

# 创建一个输出框
text1 = tk.Text(win, width=36, height=8)
text1.grid(column=0,row=5,columnspan=3)

# 输入时定焦
key_entered.focus()
# 窗口运行起来
win.mainloop()

