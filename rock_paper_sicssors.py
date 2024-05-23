#rock paper sissors
import random

def cool_logic( user_letter, computer_letter ):
    computer_val_list= [ "r" , "s" , "p" ]
    computer_index = 4
    computer_index_p1 = 0
    for a in range( 0 , 3):
        if computer_val_list[a] == computer_letter:
            computer_index = a
            print( computer_index) 
            
            
    if computer_index+1 == 3:
        computer_index_p1 = 0
    else: 
        computer_index_p1 = computer_index + 1
    
    if user_letter == computer_val_list[ computer_index] :
        return 0 #tie 
        
    if user_letter == computer_val_list[ computer_index_p1] :
        return -1 #lost

    if user_letter == computer_val_list[ computer_index-1] :
        return 1 #win
        

def do_winning_logic( user , computer ):
    if( user == computer): 
        return 0 
    
    if( user == "r" and computer == "s") :
        return 1 

    
    if( user == "r" and computer == "p") :
        return -1 
    if( user == "s" and computer == "r") :
        return -1 
    
    if( user == "s" and computer == "p") :
        return 1 
        
    if( user == "p" and computer == "r") :
        return 1 
    
    if( user == "p" and computer == "s") :
        return -1 
    
def report_on_match( val):
    if  val == 0:
        print( "tie. No points lost or gained")
        
    if  val == 1:
        print( "Human won! Human got a point")
        
    if  val == -1:
        print( "Human lost! Human lost a point")
        


print("welcome to rock paper sissors smack down best of 3! type r for rock, p for paper, s for scissors")
computer_val_list= [ "r" , "s" , "p" ]
user_points = 0
for a in range( 0 , 3):
    print( "type your choice now " )
    player_val = input() 
    computer_val = random.choice( computer_val_list) 
    print( "computer plays " + computer_val )
    match_out =  cool_logic( player_val , computer_val)
    report_on_match( match_out)
    user_points = user_points + match_out

print(" ")
print( " In the end, you got " + str(user_points) + " points")




