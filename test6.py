from random import randint, sample

sample('abcdefg', 3)#随机取样


s1 = {x:randint(1,4) for x in sample('abcdefg', randint(3,6))}
print(s1)
s2 = {x:randint(1,4) for x in sample('abcdefg', randint(3,6))}
print(s2)
s3 = {x:randint(1,4) for x in sample('abcdefg', randint(3,6))}
print(s3)

res = []

for k in s1:
	if k in s2 and k in s3:
		res.append(k)

print(res)

print(s1.keys() & s2.keys() & s3.keys())

map(dict.keys,[s1,s2,s3])

from functools import reduce

print(reduce(lambda a,b:a & b,map(dict.keys,[s1,s2,s3])))
