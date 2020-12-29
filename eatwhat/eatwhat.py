#-*- coding: UTF-8 -*-
# code by python3
# filename : eatwhat.py
# target : 用来解决中午吃饭的时候选择吃什么的问题
# author: alee
# 实现原理：通过随机数生成目标餐馆，在利用字典匹配餐馆名称，输出中午前往的餐馆地址。

import random
import time

# 获取外部文件列表
path = r'store_name.txt'
store_list = open(path, 'r', encoding='utf-8')
store_name_list = store_list.read()
store_list.close()
# 已换行符为界定，形成数组
store_name = store_name_list.split('\n')
# 删除数组中的空值
while '' in store_name:
	store_name.remove('')
# 循环五次，后退出
for i in range(5):
	restaurant_num = random.randint(0,(len(store_name)-1))
	restaurant_name = store_name[restaurant_num]
	print('')
	print('=====================================')
	print('当前的随机餐馆是： '+ restaurant_name)
	print('就它了请输入：0，再来一次请输入：1')
	print('=====================================')
	select_num = input('是否需要重新选择：')
	select_num = int(select_num)
	if select_num == 0:
		break

print('都选五次了，还选什么选！就最后一个了！')
time.sleep(3);
