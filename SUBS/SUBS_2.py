#Rosalind problem "Combing Through the Haystack" -- KNP algorithm

from sys import argv

script, filename = argv

file_in = open(filename)

s = file_in.readline()
t = file_in.readline()

def check_equal (m, n, s, t):
    return s[m + n] == t[n]
    
def check_pos ( m, n, j, k, s, t):
    
    if ( check_equal(m, n, s, t) ):
         
        if ( n == len(t) - 1 ):
        #this is the last index of a potential substring
            return True
        
        elif ( n + m > m ):
            #We are checking an index which could be the next location 
            #On return, n is set to the next index of t to check
            #On return, j is set to the next position to check
            
            if (check_equal(j, k, s, t)):
                #This location is still a possible match    
                k = k + 1
        
            else:
                #This is not a next position, go to the next 
                j = j + 1
            
        return check_pos (m, n + 1, j, k, s, t )
    
    else:
        
        return False

#indices for currently tested position
m = 0  #testing "location"
n = 0  #currently tested t index

#index for next possible position
j = 1  #next "location", if no matches it is the next index
k = 0   #next index to start testing at

positions = []

for i in s:

    if check_pos(m, n, j, k, s, t):
        positions.append(str(m + 1))
    
    #j is next "location" to test, k is the next index to test
    m = j
    n = k
    
    #reset variables for "next position" testing
    j = m + 1
    k = 0 

file_out = open("results_2.txt", "w" )

j = 0

while j < len(positions):

    file_out.write(str(positions[j]))
    file_out.write(" ")
    j = j + 1

file_in.close()
file_out.close()