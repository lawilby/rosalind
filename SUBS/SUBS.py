#Rosalind problem "Combing Through the Haystack"

from sys import argv

def check_equal (current, s, t):
    return s[current] == t[current - loc]


def check_pos ( loc, current, s, t):

    if ( (current == loc + len(t) - 2) and check_equal(current, s, t)):
    
        #this is the last index of a potential substring
        return True

    elif ( check_equal(current, s, t) ):

        return check_pos (loc, current + 1, s, t )
    
    else:
        
        return False
        


script, filename = argv

file_in = open(filename)

s = file_in.readline()
t = file_in.readline()

loc = 0 #location of potential substring we are checking
current = loc 
positions = []

for i in s:
    
    if check_pos(loc, current, s, t):
        positions.append(str(loc + 1))
    loc = loc + 1
    current = loc

file_out = open("results.txt", "w" )

j = 0

while j < len(positions):

    file_out.write(str(positions[j]))
    file_out.write(" ")
    j = j + 1

file_in.close()
file_out.close()








