letters = ["a","b","c","d","e","f","g","h","i","j","k", "l","m","n", "o","p","q","r","s","t","u","v","w","x","y","z"]
for a in range( 0 , len(letters)):
    print( letters[a])

print( "-------------|")

for a in range( 0 , len(letters)):
    if( 2*a) < len(letters):
        print( letters[2*a])

print( "-------------|")
u = input()
u = int(u) 

for a in range( 0 , len(letters)):
    if( u*a) < len(letters):
        print( letters[u*a])
