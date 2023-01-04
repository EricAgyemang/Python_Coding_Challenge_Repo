def exp(x,n):
	dn = 1; result = 1
	for i in range(1,n+1):
		dn *= i
		result += x**i/dn
	return result	