class Student(object):
	"""docstring for Student"""
	def __init__(self,  name, score):
		self.name = name
		self.score = score
		


#创建类实例
bart = Student('Michal',90)
print(bart.name)

def print_score(std):
	print('%s: %s' % (std.name, std.score))

		
print_score(bart)


def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

print(get_grade(bart))


