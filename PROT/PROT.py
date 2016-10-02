#Rosalind Problem "Translating RNA into Protein"

from sys import argv

script, filename = argv

file_in = open(filename)

s = file_in.read()

RNA_table = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "UAU": "Y", "UAC": "Y", "UAA": "\n", "UAG": "\n", "UGU": "C", "UGC": "C", "UGA": "\n", "UGG": "W", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L", "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T", "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R", "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A", "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E", "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

#Separate into codons

codes = []
i = 0

while i < len(s):

	code = s[i] + s[i+1] + s[i+2]
	codes.append(code)
	i += 3
	
file_out = open("result.txt", "w")

for i in codes:

	file_out.write(str(RNA_table[i]))
	
file_in.close()
file_out.close()

