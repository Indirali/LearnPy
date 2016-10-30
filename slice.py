
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
		
print(L[0:3])
#如果第一个索引是0可以省略
print(L[:3])

print(L[-2:])
print(L[-2:-1])

L = list(range(100))

print(L[:10])
print(L[-10:])
print(L[10:20])
print(L[:10:2])#前十个，每两个取一个
print(L[::5])#所有数每五个取一个

#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
t = (0,1,2,3,4,5,6,7,8,9)
print(t[:3])

#字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
print('ABCDEFG'[:3])

list(range(1, 11))

#列表生成式
print([x*x for x in range(1,11)])

print([x * x for x in range(1, 11) if x % 2 == 0])
#生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])

import os
print([d for d in os.listdir('.')])# os.listdir可以列出文件和目录

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)

for i in d:
	print(i)

print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']

print([x.lower() for x in L])


#测试
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
print(L2)



