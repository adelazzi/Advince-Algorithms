import time
a = 0
b = 100000
k = 0
data = list(  range( a, b ) )

n=len(data)
st = time.process_time()

for  i  in range( n-1 ):
    swapped = False
    for   j  in range(0 , n-i-1 ):
        k=k+1
        if data[ j ] <  data[ j+1 ]:
            swapped = True
            data[ j ], data[ j+1 ] =  data[ j+1 ], data[ j ]
    if not swapped:
       break
    
et = time.process_time()
print("pour N = ", n)
print("temps = ", et-st)
print( "iter = ", k )

