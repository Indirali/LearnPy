def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x

#pass占位符，还没想好的代码可以使用pass占位，程序不会出错
def nop():
	pass

age = 10
if age >= 18:
	pass

#进阶，判断进入字符类型
def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

import math

#返回多个值
def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx,ny
#假象，其实返回一个值，返回的是一个tuple


#如果有必要先对参数类型进行检查
#函数体内可以随时使用return随时返回函数结果
#函数执行完毕后也没有return时，自动return None
#函数可以返回多个值，其实就是一个tuple


#测试

import math

def quadratic(a=2,b=3,c=4):
	x = 2*b-4*a*c
	if x<0:EOF when reading a line
		return ('None')
	else:
		n=((-b+math.sqrt(x))/(2*a))
		m=((-b-math.sqrt(x))/(2*a))
		return n,m


# a = int(input('please input number a:'))
# b = int(input('please input number b:'))
# c = int(input('please input number c:'))

print(quadratic())