from random import randint

data = [randint(0,10) for _ in range(30)]

print(data)
#统计元素出现的频率

c = dict.fromkeys(data,0)
print(c)

for x in data:
	c[x] += 1
print(c)

from collections import Counter
c = Counter(data)
print(c[10])

print(c.most_common(3))
