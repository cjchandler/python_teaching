lamp_setting_1 = 0 
lamp_setting_2 = 1
lamp_setting_3 = 0 
lamp_setting_4 = 0 

lamp_list = [ 0 , 1 , 0 , 0 ] 
letter_list = [ "a" , "b" , "c" , "d"] 

print( lamp_list)
print( "lamp_list_1 ")

for a in range(0 , 4):
    
    print( lamp_list[a] ) 


def check_if_divisible_by_3( g):
    for a in range( 1 , g):
        ##3*a == g?
        if( 3*a == g):
            return True
        else:
            pass
        
    return False 
            

def check_if_prime( n):
    for a in range( 1 , n-1):
        for b in range( 1 , n-1 ):
            if( a*b == n ):
                return False 
            
    return True

list_of_primes = []
for a in range( 0 , 100):
    if( check_if_divisible_by_3(a) == True ):
        list_of_primes.append(a)
    
    
print( list_of_primes)
    
    
