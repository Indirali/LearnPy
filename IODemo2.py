from io import StringIO

#在内存中写入str
f = StringIO()
f.write('hello')
print(f.getvalue())

f=StringIO('Hello!\nHi!\nGoodBye!')
while True:
	s = f.readline()
	if s=='':
		break
	print(s.strip())

#操作二进制数据
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

