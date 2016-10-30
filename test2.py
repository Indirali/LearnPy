#定义元祖的每个属性的名字，提高可读性
student = ('Jim',16,'male','1234567@163.com')

NAME,AGE,SEX,EMAIL = range(4)

print(student[NAME])
print(student[AGE])


from collections import namedtuple
Student = namedtuple('Student',['name','age','sex','email'])

s = Student('Jim',16,'male','1234567@163.com')
print(s)
print(s.name)

