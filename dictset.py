names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]

#dict其他语言也称为map,使用键-值（key-value）存储，具有极快的查找速度。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

d['Adam'] = 67
print(d['Adam'])

#由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉

d['Jack'] = 90
print(d['Jack'])
d['Jack'] = 88
print(d['Jack'])

#dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
print(d.get('Thomas'))
print(d.get('Thomas', -1))

#要删除一个key，用pop(key)方法，对应的value也会从dict中删除
d.pop('Bob')
print(d)

#list比较，dict有以下几个特点：

#查找和插入的速度极快，不会随着key的增加而变慢；
#需要占用大量的内存，内存浪费多。


#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set([1, 2, 3])
print(s)

#添加一个set,可以重复添加，但不会有效果
s.add(4)
print(s)

#删除元素
s.remove(4)
print(s)

#交集和并集操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])

print(s1&s2)#交集
print(s1|s2)#并集

a = ['c', 'b', 'a']
a.sort()
print(a)

a = 'abc'
b = a.replace('a', 'A')
print(b)#a仍是'abc'




