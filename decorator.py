#在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
	print('2016-10-14')

now()

#偏函数

int('12345', base=8)

import functools

#把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
int2 = functools.partial(int, base=2)
int2('1000000')
#使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。



