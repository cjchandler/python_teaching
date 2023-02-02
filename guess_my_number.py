#if you make a # symbol, everything after that is ignored by the computer. This is
# handy for writing notes to yourself, and explaining what the parts of the
#computer program do.

#This is an example python program where the user can play a guessing game against
#the computer

print( "Welcome to my guessing game. If you want to play, type Y. To quit type N.")

start_game = False
while( start_game == False):
    user_string = input()
    if( user_string == "Y" ):
      ##move on to play the game
      start_game = True
      continue
    if( user_string == "N"):
      #user wants to quit.
      quit() #this stops you program.
    if( user_string != "N" and user_string != "Y"):
        print("sorry, I don't understand that. type Y to play or N to quit")

###here is the game:
my_secret_number = 9
user_number = 0
while user_number != my_secret_number:
    print( "guess my secret number, type any number to try it")
    user_try = input() 
    if( int(user_try) != my_secret_number):
        print("nope, try again.")
    if( int(user_try) == my_secret_number):
        print("YES! That's it!")
        user_number = my_secret_number

print( "TaaDaa ..... You won")
quit()
