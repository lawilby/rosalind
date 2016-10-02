#Rosalind problem "Wabbit Season"

n = int(raw_input("Please enter a value for n: "))
m = int(raw_input("Please enter a value for m: "))

series = { 1: 1, 2: 1 }

def rabbits(n, m):
	
	if n in series:
		
		return series[n]
	
	if n <= 0:
		
		return 1
	
	else:
		
		series[n] = rabbits(n - 2, m) + rabbits(n - 1, m) 
		
		return series[n]
		
		
ans = rabbits(n, m)

print ans