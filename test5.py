from random import randint

sorted([9,4,3,6,2,5,6,1,7,3])
d = {x: randint(60, 100) for x in 'xyzabc'}
print(sorted(d))#只按照键排序

print(sorted(zip(d.values(), d.keys())))

print(d.items())

print(sorted(d.items(),key=lambda x: x[1]))




