
from itertools import product 
 
graphe=[[0,1,0,1,0,0,1,1],
[1,0,0,1,0,1,0,0],
[0,0,0,1,0,1,0,0],
[1,1,1,0,1,0,0,0],
[0,0,0,1,0,1,0,0],
[0,1,1,0,1,0,1,1],
[1,0,0,0,0,1,0,0],
[1,0,0,0,0,1,0,0],
]

M =[[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
]

n = len(graphe)       
#N = 2**n
s = []

def cost( s ):
    SA = 0 
    for i in range(n):
        if s[i] == '1':
            SA = SA + 1
    return   SA 

    
def const( s ):  
    global M
    cnt = 0
    for i in range(n):
        if s[i] == '1':
            for j in range(n):
                M[ i ][ j ] = 0
                M[ j ][ i ] = 0
                
    for i in range(n):
        for j in range(n):
                if M[ i ][ j ] == 1 :
                    cnt = cnt + 1
    return cnt

def initial():
    s = []
    for i in range(n):
        s.append( '1')
    return s

def copie(M,graphe):
    for i in range(n):
        for j in range(n):
             M[ i ][ j ] = graphe[i][j]
                


comb = product( ['0', '1'], repeat=n) 
c = n
s = initial()

for sp in list(comb):
    copie( M , graphe )
    x = const( sp )
    if x== 0 : 
        cp = cost( sp )
        if cp < c:
            c = cp
            s = sp 

print( s , c )
