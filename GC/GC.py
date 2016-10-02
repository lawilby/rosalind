#Rosalind problem "Identifying Unknown DNA Quickly"

from sys import argv

script, filename = argv

file_in = open(filename)

GC = {}

currentID = 0

for line in file_in:

	current = line
	print line

	if current[0] == '>':
		
		#Record results of previous tally, unless this is the first line
		if currentID != 0:
			
			print currentID
			print GC_count
			print bp_count
			GC_ratio = float(GC_count)/bp_count
			print GC_ratio
			GC[currentID] = GC_ratio
		
		#Reset counts
		GC_count = 0
		bp_count = 0
		
		#Move to next ID
		currentID = current
		
		GC[currentID] = 0
	
	else:

		for i in current:
			
			if i == 'G' or i == 'C':
				GC_count += 1
			
			if i == 'G' or i == 'C' or i == 'A' or i == 'T':
				bp_count += 1
			

#Record last tally
print currentID
print GC_count
print bp_count
GC_ratio = float(GC_count)/bp_count
print GC_ratio
GC[currentID] = GC_ratio	

max = currentID

for i in GC:
	if GC[i] >= GC[max]:
		max = i

print max
print GC[max]*100
		
print GC		