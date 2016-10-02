#Consensus and Profile: Finding a Most Likely Common Ancestor

from sys import argv

script, filename = argv

file_in = open(filename)

def print_profile ( base, count, file_out, Profile):

    file_out.write(base)
    file_out.write(": ")
    k = 0
    while k < count:
        file_out.write(str(Profile[base][k]))
        k = k + 1
    file_out.write("\n")
         

count = 0
Profile = {'A': [0]*1000, 'C': [0]*1000, 'G': [0]*1000, 'T': [0]*1000}
Consensus = []


for line in file_in:
    
    #build Profile matrix
    count = 0
    if line[0] != '>':

        for i in line:
            
            if i != "\n":
            
                Profile[i][count] = Profile[i][count] + 1
                count = count + 1

#build consensus string
i = 0
while i < count:

    candidate = "A"
    max_amnt = Profile["A"][i]
    
    if Profile["C"][i] > max_amnt: 
        candidate = "C"
        max_amnt = Profile["C"][i]
    
    if Profile["G"][i] > max_amnt: 
        candidate = "G"
        max_amnt = Profile["G"][i]
    
    if Profile["T"][i] > max_amnt: 
        candidate = "T"
        max_amnt = Profile["T"][i]
    i = i + 1
    Consensus.append(candidate)
        
file_out = open("results.txt", "w")

for i in Consensus:

    file_out.write(i)
    
file_out.write("\n")
print_profile("A", count, file_out, Profile)
print_profile("C", count, file_out, Profile)
print_profile("G", count, file_out, Profile)
print_profile("T", count, file_out, Profile)


file_in.close()
file_out.close()





         