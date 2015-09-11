

#suppose I have a, b min edit distance is either 0 or 2 for subs
#suppose I have (xy) (cd) decisions
# Either convert x --> c, ^ y--> d ^ both
# (xyz) (cde) I can: (xy) --> (cd) z--> e

#Consider the most general Case!

# x1 x2 x3 ... xN --> y1 y2 ---> yM

#There exists a partitioning of the X | x1 ... xk1 | xk1+1 ... xk2 ...| -->
#the partitioning of Y that is optimal

#How to find it ?

# Suppose I had a routine to calculate the min Edit Distance

# Min Edit Distance of paritioning x into two parts nad mapping those to adjacent Y parts
#REcursively descend

# MinEdit(1,1) + MinEdit(2,1) + MinEdit(3,1) ... MinEdit(x-1,1) +
# MinEdit(1,2) ...
# n = size of x, m = size of y
# nm layers of first level recursion and then we dsciend on each case
# ahhh !!! thats bad

# 

def mineditDist(s1,s2):
    metatab = [[]]
    i = 0
    while i < len(s1):
        metatab[0].append(i)
        i+=1
    
    i = 1
    while i < len(s1):
        metatab.append([i])
        j = 1
        while j < len(s2):
            q = metatab[i-1][j-1]
            if s1[i] == s2[j]:
                q-=2
            q+=2
            metatab[i].append(min(metatab[i-1][j]+1,metatab[i][j-1]+1,q))
            j+=1
        i+=1
    
    return metatab[len(s1)-1][len(s2)-2]

print mineditDist("sometal","someal")
         
