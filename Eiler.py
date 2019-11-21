def primdiv(n):
	res = []
	i = 2
	while i <= n:
		if n % i == 0:
			while n % i == 0:
				n//=i
			res.append(i)
		i += 1
	return res

def eiler(n):
	p = primdiv(n)
	p = list(map(lambda x: 1 - (1/x), p))
	for i in p:
		n = n * i
	return int(n)
	
n = int(input())
print(primdiv(n),' ',eiler(n))
