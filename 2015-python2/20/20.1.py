def factors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

limit = 2900000
i = 1
while True:
	if sum(factors(i)) >= limit:
		print i
		exit()
	i += 1
