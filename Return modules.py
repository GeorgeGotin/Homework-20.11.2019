def NOD(a,b):
	r = a % b
	while r != 0:
		a = b
		b = r
		r = a % b
	return b
	
def noteiler(n):
	m = 0
	for i in range(n):
		if NOD(i,n) == 1:
			m += 1
	return m

n = int(input())
print(noteiler(n))
