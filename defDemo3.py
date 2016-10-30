#一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数

def add(x,y,f):
	return f(x)+f(y)

print(add(-5,6,abs))

#map()函数接收两个参数，一个是函数，一个是Iterable
def f(x):
	return x*x

r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce
def add(x, y):
	return x + y

print(reduce(add,[1,3,5,7,9]))

def fn(x, y):
	return x * 10 + y

print(reduce(fn, [1, 3, 5, 7, 9]))



