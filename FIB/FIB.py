#A program for calculating rabbit offspring. 
#Rosalind problem "Rabbits and Recurrence Relations"

n = int(raw_input("Please enter the value of n: "))
k = int(raw_input("Please enter the value of k: "))

def rabbit(n, k):
	if n == 1:
		return 1
		
	if n == 2:
		return 1
	
	else:
		return rabbit(n-1, k) + k*rabbit(n-2, k)
	
ans = rabbit(n, k)

print ans




