def power(x):
	return x*x

print(power(2))

def power(x,n):
	s=1
	while n>0:
		s = s*x
		n = n-1
	return s

print(power(5,3))

#默认参数
def power(x,n=2):
	s=1
	while n>0:
		s = s*x
		n = n-1
	return s

#默认参数必须指向不可变对象
def add_end(L=[]):
	L.append('END')
	return L

def add_end(L=None):
	if L is None:
		L=[]
	L.append('END')
	return L

#传入一个list
def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

#调用
print(calc([1,2,3,4]))

#可变参对象
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

#调用
print(calc(1,2,3,4))

#关键字参数
#允许你传入0个或任意个含参数名的参数，这些关键朱会自动组装为一个dict
def person(name,age,**kw):
	print('name',name,'age',age,'other',kw)

print(person('Michael',30,city='Beijing'))
print(person('Michael',30,gender='M',job='Engineer'))

extra = {'city':'Beijing','job':'Engineer'}
print(person('Michael',30,city=extra['city'],job=extra['job']))

#命名关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

print(person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456))

#命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)

#命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错