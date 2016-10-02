from sys import argv

script, filename = argv

file_in = open(filename)

s = file_in.read()

dict = {'G': 'C', 'C': 'G', 'A': 'T', 'T': 'A' }
sc = []

i = len(s)-1

file_out = open('result.txt', 'w')

while i >= 0:
    
	sc.append(str(dict[s[i]]))
	
	print dict[s[i]]
	file_out.write(str(dict[s[i]]))
	i -= 1

file_in.close()	
file_out.close()
