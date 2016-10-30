class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


#两个下划线外部类访问不到属性了


#外部类想要访问属性使用get方法

	def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
#修改参数

	def set_name(self, score):
		
        self.__score = score
        

	def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


