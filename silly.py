import time 
import random 
answers = [ "Sorry, nope" , "Not today" , "just sold out"  , "Nah, I've never sold that!" , "what do you think I am, a geanie?"  ]


print( " hello and welcome to my store" ) 
print ( "I have many things for sale, would you like to see the list?") 
time.sleep(2) 
print( "You know, I forgot where I put the list. Just ask me stuff and I'll see if i have it") 
while True: 
    q = input()
    print( random.choice(answers) )
 
