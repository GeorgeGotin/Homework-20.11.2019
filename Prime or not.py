def primq(p):
	for i in range(2,int(p ** 0.5)):
		if p % i == 0:
			print('Not prime')
			return i
	print('Prime')
	return(1)

n = int(input())
print(primq(n))
		
