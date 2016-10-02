#Rosalind problem "Counting Point Mutations"

from sys import argv

script, filename = argv

file_in = open(filename)

s = file_in.readline().rstrip()
t = file_in.readline().rstrip()

i = 0
dH = 0

while i < len(s):
	
	if s[i] != t[i]:
	    dH += 1
    
	i += 1
    


print dH