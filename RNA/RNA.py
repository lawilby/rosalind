from sys import argv

script, filename = argv

in_file = open(filename)

t = in_file.read()
u = []

for letter in t:
	if letter == 'T':
		u.append('U')
	else:
		u.append(letter)
	
out_file = open('result.txt', 'w')

for i in u:

	out_file.write(i)
	print i

out_file.close()
in_file.close()


