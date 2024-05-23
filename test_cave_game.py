#test cave game 
import cv2

current_room_name = "A"
n_matches = 0
player_alive = True

def move( room_name , direction ): 
    if( room_name == "A" ):
        if( direction == "N" or direction == "S" ): 
            print( "you hit a wall")
            return "A"
        if( direction == "W" ): 
            print( "you move down a damp tunnel")
            return "C"
        if( direction == "E" ): 
            print( "you move down a damp tunnel")
            return "B"
    if( room_name == "B" ):
        if( direction == "N" or direction == "S" or  direction == "E"): 
            print( "you hit a wall")
            return "B"
        if( direction == "W" ): 
            print( "you move down a damp tunnel")
            return "A"
        
            
def room_action( room_name ): 
    player_alive_status = True
    if room_name == "A":
        print( "you are in a tunnel with oepnings to the eash and west") 
        return True
    if room_name == "B":
        print( "it's a dead end ")
        return True 
    if room_name == "C":
        print( "you find your way out , yay you win")
        return False 
    
    return 


def load_pic( filename):
    img = cv2.imread(filename)
    scale_percent = 60 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
      
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return resized    

def use_match( room_name ):
    if( room_name == "A"):
        img_A = load_pic('/home/carl/Git_Projects/python_teaching/hall_carlA.jpeg')
        
        cv2.imshow(' ', img_A)
    if( room_name == "B"):
        img_B = cv2.load_pic('/home/carl/Git_Projects/python_teaching/dead_guy_carlB.jpeg')
        cv2.imshow(' ', img_B)
    if( room_name == "C"):
        img_C = cv2.load_pic('/home/carl/Git_Projects/python_teaching/stairs_carlC.jpeg')
        cv2.imshow(' ', img_C)
     
    cv2.waitKey(1000) 
    cv2.destroyAllWindows() # destroys the window showing image
    return 

print( "you awake in the dark") 
player_alive = room_action( current_room_name )

while player_alive == True: 
    print( "type N,S,E,W to move, m to use match")
    desired_direction = input()
    if( desired_direction == "m"):
        use_match(current_room_name) 
    else: 
        current_room_name = move( current_room_name , desired_direction)
        player_alive = room_action( current_room_name )

