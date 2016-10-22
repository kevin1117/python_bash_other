# coding=utf-8

import os

import datetime

dir = "aa.txt"
if os.path.exists(dir):
    os.remove(dir)

f = open('aa.txt', 'a+')

now = datetime.datetime.now()
f.write(now.strftime('%Y-%m-%d %H:%M:%S')+"\n")
f.seek(0)
# 打印出来的是一个文件句柄信息:<_io.TextIOWrapper name='aa.txt' mode='r' encoding='utf-8'>
# print(f.read())  # 打印出来的就是文件所有的内容,全部加载到内存,读取出来
print('line1:' + f.readline()),  # 打印的是文件第一行的内容

f.write(now.strftime('%Y-%m-%d %H:%M:%S')+"\n")
f.seek(0)

arr = f.readlines()  # 把文件内容每行当做一个列表的元素,放到一个列表中,打印的是一个列表
print(arr.__len__())
for ll in arr:
    print(ll),

f.close()
