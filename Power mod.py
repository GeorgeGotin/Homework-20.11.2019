import random

def power_mod(a,b,n):
	a %= n
	res = a
	for i in range(b - 1):
		res *= a
		res %= n
	return res
print('Write a,b and n for \n a^b %n:\na = ',end ='')
a = int(input())
print('b = ',end ='')
b = int(input())
print('n = ',end ='')
n = int(input())
#a = random.randint(2,10000)
#b = random.randint(2,10000)
#n = random.randint(2,10000)
print('{} {} {}'.format(a,b,n))
print(power_mod(a,b,n))
