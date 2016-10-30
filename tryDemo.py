import logging

try:
	print('try...')
	#r = 10/0
	r = 10/int('a')
	print('result',r)
except ValueError as e:
	print('ValueError',e)
except ZeroDivisionError as e:
	print('except:',e)
	logging.exception(e)
else:
	print('no error!')
finally:
	print('finally...')
print('END')	


#调试方法
#assert断言
def foo(s):
	n = int(s)
	assert n!=0,'n is zero!'
	return 10/n

def main():
	foo('0')

#main()
#assert的意思是，表达式n!=0应该是true，否则后面的逻辑代码一定出现错

#使用logging不会抛出错误
import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' %n)
#print(10/n)

#python调试器pdb
import pdb
s = '0'
n = int(s)
print(10/n)










