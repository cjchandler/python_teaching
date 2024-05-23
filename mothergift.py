#####function to ask for favorite _________ ######
def funcquest( word):
    print( "What is your mother's favorite " + word + " ?")
    a = input()
    return a
    
#####function to make a word plural
def pluralize(singular_word):
    last_letter = singular_word[-1]
    plural_word = "butts"
    
    if( last_letter =='s'):
        plural_word = singular_word + "es"
    
    if( last_letter == 'y'):
        root_word = singular_word[:-1]
        plural_word  = root_word + "ies"
        
    if( last_letter != "y" and last_letter != "s"):
        plural_word = singular_word + "s"
    
    return plural_word

#####functon to check if input is a number    
def check_input_is_number( a):
    try:
        a = int(a)
        return True
        
    except:
        print( "I don't understand that number, try an integer")
        return False


print( "Welcome to gift select 2000, we will find the best gift for your mother.")
fav_thing = funcquest( "thing")

fav_number = 9.9
is_int_number = False
while is_int_number == False: 
    fav_number = funcquest("number")
    is_int_number = check_input_is_number(fav_number)

fav_color = funcquest("color")
fav_shape = funcquest("shape")

if( int(fav_number) > 1):
    fav_thing = pluralize(fav_thing)
    
print("You should get her " + fav_number + " " + fav_color + " " + fav_shape + " " + fav_thing +".")

