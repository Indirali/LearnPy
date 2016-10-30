#filter()函数用来过滤序列
#filter不接收一个函数和一个序列，把传入的元素依次作用于每个元素，根据返回值是true,false来决定保留还是丢弃元素

def is_odd(n):
	return n % 2 == 1

print(list(filter(is_odd,[1,2,3,4,5,6,7,8])))


def not_empty(s):
	return s and s.strip()

print(list(filter(not_empty,['A','','B',None,'C',' '])))

#求素数
def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

def _not_divisible(n):
	return lambda x: x%n >0

def primes():
	yield 2
	it = _odd_iter() #初始化序列
	while True:
		n = next(it)#返回序列的第一个数
		yield n
		it = filter(_not_divisible(n), it)#构造新序列


for n in primes():
	if n < 1000:
		print(n)
	else:
		break
#结束

#测试

def is_palindrome(n):
	return int(str(n)[::-1]) == n

output = filter(is_palindrome,range(1,1000))
print(list(output))


#sorted()排序算法
#sorted()也是一个高阶函数可以接收一个key来实现函数自定义排序

print(sorted([36,5,-12,9,21]))

print(sorted([36,5,-12,9,21],key=abs))

#进行反向排序reverse=True
print(sorted([36,5,-12,9,21],key=abs,reverse=True))


L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]

def by_name(t):
	return t[0].lower()

L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
	return t[1]

L2 = sorted(L,key=by_score,reverse=True)
print(L2)





