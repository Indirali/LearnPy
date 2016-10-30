
f = open('E:\python工程\Mtest.txt','r')
print(f.read())


try:
	f = open('E:\python工程\Mtest.txt','r')
	print(f.read())
finally:
	if f:
		f.close()

with open('E:\python工程\Mtest.txt','r') as f:
	print(f.read())

#如果文件很大会报错，一次调用小部分比较保险
	for line in f.readlines():
		print(line.strip())#把末尾的'\n'删掉

import re
#二进制文件
f = open(r'C:\Users\lenove\Pictures\Saved Pictures\test.jpg','rb')
print(f.read())
f.close

#有些编码不贵发的文件，加一个参数errors，最简单的办法是直接忽略
f = open('E:\python工程\Mtest.txt','r',encoding='gbk',errors='ignore')
f.close


#写入
f = open('E:\python工程\Mtest.txt','w')
f.write('Hello,world!')
f.close


