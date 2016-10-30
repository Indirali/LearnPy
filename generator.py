#这种一边循环一边计算的机制，称为生成器：generator

g = (x * x for x in range(10))
print(g)
#一个一个打印出来，可以通过next()函数获得generator的下一个返回值
print(next(g))

for n in g:
	print(n)

#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

def triangles():
    L = [1]
    while True:
        yield L
        L1 = [0] + L[:]
        L = [L[i]+L1[i] for i in range(len(L))] + [1]

def triangles():
    L = [1]
    while True:
        yield L
        L.append(0);
        L = [L[i-1] + L[i] for i in range(len(L))]
