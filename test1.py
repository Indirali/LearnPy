#过滤数据，提高效率

from random import randint

data = [randint(-10,10) for _ in range(10)]

print(data)

n = filter(lambda x: x >= 0, data)#第二
m = [x for x in data if x >= 0]#最快
#迭代最慢
print(n)
print(m)


d = {x: randint(60, 100) for x in range(1,11)}
print(d)

print({k: v for k,v in d.items() if v > 90})

s = set(data)
x = {x for x in s if x%3==0}
print(x)