import random

n = random.randint(0, 26)

abc_list = [ 'a','b','c' , 'd' , 'e' , 'f' , 'g' , 'h' ,'i' ,'j' ,'k' ,'l' ,'m' ,'n' ,'o' ,'p' ,'q' ,'r' ,'s' ,'t', 'u', 'v', 'w', 'x' ,'y' ,'z']  

print ("hello kid " )
print( "what is the " +  str(n)  + "th letter of the alphabet? " ) 
k = input() 
if( k.lower() == abc_list[n-1] ):
    print( " you are correct" ) 
else: 
    print( "you fail" )
