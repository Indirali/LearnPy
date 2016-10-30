
#返回函数
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

#当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
f = lazy_sum(1, 3, 5, 7, 9)


#匿名函数lambda

f = lambda x: x * x
print(f(5))

#可以把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y

f = build(1, 2)
print(f())



