def puissance(x, n):

    if n == 0:
        return 1
    if n == 1:
        return x
    

    if n % 2 == 0:

        return puissance(x, n // 2) * puissance(x, n // 2)
    else:

        return puissance(x, (n - 1) // 2) * puissance(x, (n - 1) // 2) * x

x = puissance(2, 2)
print(x)  
print(2**2) 


