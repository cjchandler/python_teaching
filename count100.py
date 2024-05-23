# ~ for a in range( 1 , 100): 
    # ~ print( a) 

print ( "type a number to count by")
n = input()
n = float(n)

for a in range( 1 , 100): 
    
    if n*a >= 100:
        exit() 

    print( n*a)
