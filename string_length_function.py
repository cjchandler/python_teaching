import cv2

def load_pictures(): 
    img_test = cv2.imread('/home/carl/Git_Projects/python_teaching/banban.jpeg')

    dict_of_pictures = {}
    dict_of_pictures["picture of banban"] = img_test
 
    return dict_of_pictures

current_room_name = "A" 
current_direction = "N" 
n_matches = 10 
player_alive = True
dict_of_pictures = load_pictures()


 
def show_picture( dict_of_pictures , picture_name_to_show ):
 
    cv2.imshow(' ', dict_of_pictures[picture_name_to_show] )
     
    cv2.waitKey(3000) 
    cv2.destroyAllWindows() # destroys the window showing image
    return 

def listen_for_player_input():
    i = input()
    
    #turn right 
    #turn left
    #turn 180
    
    #go forward
    if i == "go forward": 
        print( " Your pancreas is ripped from your side. Game Over")
        player_alive = False
        
    
    #light match
    if i == "light match": 
        show_picture( dict_of_pictures , "picture of banban") 
        
    #help
    list_of_commands = ["turn right" , "turn left" , "go forward" , "light match" , "help"]
    
    if i == "help" :
        print( " these are the commands that the computer understands" )
        print(list_of_commands)
    

    
    return


print( " You awake in a dark space. In your hand you feel a packet of matches. What do you do next? ")
while player_alive == True: 
    listen_for_player_input()





quit()

import cv2

 
img = cv2.imread('/home/carl/Git_Projects/python_teaching/banban.jpeg')
 
cv2.imshow('test picture',img)
 
cv2.waitKey(3000) 
cv2.destroyAllWindows() # destroys the window showing image

quit()



#MAKE A FUNCTION
def my_length_function(input_string):
    input_string = input_string.replace( " " , "")
    print(input_string)
    output = len(input_string)
    return output 

character_list = [ "jester" , "banban" , "tarta bird" , "tamataki" , "chamataki" ]

for a in character_list:
    print( " character name is " , a , " and the number of letters is " , my_length_function(a) ) 


def insult( name) :
    if( name.lower() == "carl" ): 
        return " Carl is cool" 
    else: 
        return name + " is a poop head"
        
        
def insult2( name , friend_list):
    if( name.lower() in friend_list ) == True: 
        return name + " is cool" 
    else: 
        return name + " is a poop head"
        
while True: 
    print( "type in your name" )
    n = input()
    print( insult2(n , ["isaac" , "harang" , "carl", "andy" , "catherine"] ))



