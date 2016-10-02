from sys import argv

script, filename = argv

out = open("result.txt", 'w')

letters = { 'A': 0, 'C': 0, 'G': 0, 'T': 0 }

string = open(filename).read()  

for letter in string:
    letters[letter] += 1

print letters['A'], letters['C'], letters['G'], letters['T']


out.write( str(letters['A']) )
out.write(" ")
out.write( str(letters['C']) )
out.write(" ")
out.write( str(letters['G']))
out.write(" ")
out.write( str(letters['T']))

out.close()




	
