def isprime(i):
    for a in range( 2 , i):
        for b in range( 2 , i):
            if a*b == i:
                return( a, b) 
    # ~ print( "yep, is prime")
    return( -1, -1)
    
# ~ x,y = isprime(17)
# ~ print( x,y)

for a in range( 0 , 1000000):
    x,y = isprime(a)
    if( x == -1 and y == -1):
        print( a)
