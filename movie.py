import time

def print_new_lines( n ):
    for a in range( 0, n):
        print( "")

def add_spaces(l):
    out = ""
    for a in range( 0, l):
        out += " "
    
    return out

p = 0 
while True : 
    if p <19:
        thing = "#==>"
    if p == 19:
        thing =  "<<<BOOM>>>"
        
    mstring =     "   <=>----"
    bottomstring ="[ooooo]"
    mstring = mstring+ add_spaces( p ) + thing
    print( mstring )
    print(bottomstring)
    print_new_lines(21)
    time.sleep(0.1)
    p = (p + 1 )%20
    
