import time

aList=[]
iter =0
def search(a ,b, key):
    global iter
    iter = iter+1
    for i in range(100):
       
        mid = int( (a+b) / 2)
        #print("Searching midpoint at ", str( aList[mid]) )
        if mid == 0:
            print("Key Not Found!" )
            return key
        elif key == aList[mid]:
             #print("Key Found! at position : " + str(mid) )
             return aList[mid]
        elif key > aList[mid]:
             #print( a, b )
             a=mid+1
             search( a, b, key )
        else:
             #print( a, b )
             b = mid -1
             search( a, b, key )
    
a=0
b=100000

k=2
#k=0000000


aList = list(range(a, b))
st = time.process_time()
search( a, b, k)
et = time.process_time()

print("Pour N = ", len( aList) )
print("Temps = " , et-st)
print( "iter = ", iter )
