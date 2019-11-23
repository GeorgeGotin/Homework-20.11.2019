import random

def fastpower_mod(a,n,b):
	a %= b
	m = []
	while n > 0:
		m.append(n%2)
		n = n // 2
	s = 1
	q = len(m)
	for i in range(q):
		if m[q - i - 1] == 0:
			s = (s*s) % b
		else:
			s= (s*s*a) % b
	return s

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
print(fastpower_mod(a,b,n))

