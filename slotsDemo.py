class Student(object):
	pass



s = Student()
s.name = 'Michael'#动态给实例定义一个属性
print(s.name)

def set_age(self,age):
		self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s)#给实例绑定一个方法，这个方法在其他实例中无法使用
s.set_age(25)
print(s.age)


#__slots__限制class实例能添加属性

class Teacher(object):
	__slots__ = ('name','age')#用tuple定义允许绑定的属性名称


t = Teacher()
t.name = 'Jenney'
t.age = 54
t.job = 'python'

#使用__slots__仅对当前类实例起作用个，对继承的子类是不起作用的

		