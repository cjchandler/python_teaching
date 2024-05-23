

def show_bodycount_6():
    print( "____" )
    print( "|   |")
    print( "|   O")
    print( "|  -|-")
    print( "|  /\ ")
    print( "|________")
    

def show_bodycount_5():
    print( "____" )
    print( "|   |")
    print( "|   O")
    print( "|  -|-")
    print( "|  / ")
    print( "|________")
    
def show_bodycount_4():
    print( "____" )
    print( "|   |")
    print( "|   O")
    print( "|  -|-")
    print( "|   ")
    print( "|________")
    
def show_bodycount_3():
    print( "____" )
    print( "|   |")
    print( "|   O")
    print( "|  -|")
    print( "|   ")
    print( "|________")

def show_bodycount_2():
    print( "____" )
    print( "|   |")
    print( "|   O")
    print( "|   |")
    print( "|   ")
    print( "|________")
    
def show_bodycount_1():
    print( "____" )
    print( "|   |")
    print( "|   O")
    print( "|   ")
    print( "|    ")
    print( "|________")

def show_bodycount_0():
    print( "____" )
    print( "|    ")
    print( "|    ")
    print( "|    ")
    print( "|    ")
    print( "|________")


# ~ line1 =  "____"
# ~ line2 =  "|   |"
# ~ line3_empty =  "|   "
# ~ line3_A =  "|   O"
# ~ line4_empty =  "|  "
# ~ line4_B =  "|   |"
# ~ line4_C =  "|  -|"
# ~ line4_D =  "|  -|-"
# ~ line5_empty = "|   "
# ~ line5_E = "|   \ "
# ~ line5_F = "|  /\ "
# ~ line6 = "|________"



def user_input( list_of_user_guesses , body_count):
    inchar = input(  )
    list_of_user_guesses.append( inchar) 
    if ( inchar in secret_word) != True:
        body_count = body_count + 1 
        
    return list_of_user_guesses, body_count

def show_hangman( body_count):
    if(  body_count ==0   ):
        show_bodycount_0()
    if(  body_count ==1   ):
        show_bodycount_1()
    if(  body_count ==2   ):
        show_bodycount_2()
    if(  body_count ==3   ):
        show_bodycount_3()
    if(  body_count ==4   ):
        show_bodycount_4()
    if(  body_count ==5   ):
        show_bodycount_5()
    if(  body_count ==6   ):
        show_bodycount_6()

def show_blanks( secret_word , list_guesses ):
    out_string = ""
    for a in range( 0 , len(secret_word)):
        if( (secret_word[a] in list_guesses)== True ):
            out_string = out_string + " " +secret_word[a]+" " 
        else:
            out_string = out_string + " _ "
            
    return out_string

guess_index = 0 

def human_win( secret_word , list_guesses):
    out_string = show_blanks( secret_word , list_guesses )
    if( "_" in out_string ):
        return False
    else:
        return True
        
def computer_win( body_count ):
    if body_count < 6 :
        return False
    else:
        return True

print( " Welcome to hangman!")
print( "Guess one letter at a time") 
secret_word = "dog" 
list_of_user_guesses = [  ] 
body_count = 0
import time
while True:
    #let the user type
    # ~ print( "here is where I will put code to let the user type")
    print( "Type your guess")
    list_of_user_guesses, body_count  = user_input( list_of_user_guesses, body_count)

    #show hang man 
    
    # ~ print( "here is where I will put code to show the current hangman")
    show_hangman( body_count)
    #show the blanks 
    # ~ print( "now I show the blanks")
    out = show_blanks( secret_word , list_of_user_guesses )
    print( out)
    
    #check if human won- if yes, end game 
    if( human_win( secret_word , list_of_user_guesses ) ):
        print( "You won")
        exit()
    
    #chcek if computer won- if yes end game
    if( computer_win( body_count) ):
        print( "You Lost" )
        exit()
    time.sleep(1)
    
list_of_user_guesses, body_count  = user_input( list_of_user_guesses, body_count)
show_blanks( secret_word , list_of_user_guesses)
