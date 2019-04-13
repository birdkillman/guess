import random
a = input('请输入最小范围： ')
b = input('请输入最大范围： ')
a = int(a)
b = int(b)
r = random.randint(a, b)
x = 1
while True:
	print('第', x, '次机会')
	a = input('请输入数字： ')
	a = int(a)
	x = x + 1
	if a == r:
		print('答对了')
		break
	elif a > r:
		print('比答案大')
	else:
		print('比答案小')
