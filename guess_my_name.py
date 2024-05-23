print("player 1, enter your name")
x = input()
print("player 2, you have 5 guesses to find the name")
n_guesses = 0 
max_guesses = 5 

for a in range( 0 , 5):
	print( "this is your " , a , " th guess")
	y = input()
	if( y == x ):
		print( " you got it!")
		exit()
	else: 
		print( " you are wrong")
