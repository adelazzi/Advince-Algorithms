import time

aList=[]
iter=0

def search( key ):
    global iter
    
    for i in range( len( aList) ):
        iter = iter + 1
        if aList[i] == key :
            return i

    return -1 
    
a = 0
b = 100000

k = 2
#k=b-1

aList = list(  range( a, b ) )

st = time.process_time()
print( search( k ) )
et = time.process_time()

print("Pour N = ", len( aList) )
print("temps = ", et - st)
print( "iter = ", iter )



