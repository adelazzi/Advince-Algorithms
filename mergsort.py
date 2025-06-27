from heapq import merge


def mergeSort( listt ):
    if len(listt) < 2:
      return listt
    middle = len(listt)//2
    left = mergeSort( listt[ :middle ] ) # [ 0 : middle]
    right = mergeSort( listt[ middle: ] )
    merged = [left,right]
  
    return merged

liste =[5,6,4,8,7,9,2]
liste2=mergeSort( listt=liste )
print(liste)
print(liste2)