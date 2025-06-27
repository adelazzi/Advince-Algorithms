# -*- coding: utf-8 -*-


graph =     [[0,1,0,1,0,0,1,1],
             [1,0,0,1,0,1,0,0],
             [0,0,0,1,0,1,0,0],
             [1,1,1,0,1,0,0,0],
             [0,0,0,1,0,1,0,0],
             [0,1,1,0,1,0,1,1],
             [1,0,0,0,0,1,0,0],
             [1,0,0,0,0,1,0,0],
            ]

def vide( g ):
    for i in range(len(g)):
        for j in range (len(g[i])):
            if g[i][j] != 0 :
                return False 
    return True

def choix( g ):
    nc    = 0
    choix = 0
    
    for i in range(len(g)):
        n=0
        for j in range (len(g[i])):
            if g[i][j] != 0 :
                 n = n+ 1
        if n > nc:
            nc = n
            choix = i
    return choix

def remove( g, u ):  
    for i in range(len(g)) :   
            g[u][i] = 0
            g[i][u] = 0
    return g 
       
#------------------------
c = []
while not vide(graph) :
        n = choix(graph) 
        c.append(n)
        remove(graph,n)
       
print( graph )
print( c )

