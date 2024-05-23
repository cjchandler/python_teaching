print( "welcome to typemaster 5000")
import time 



list_of_sentences =  [ "my cat is green" , "my cat is sick" , "my cat ate a hat" , "that was not a good idea", "now my cat may puke"]




class game:
    def __init__(self , list_of_sentences):
        self.list_of_sentences = list_of_sentences
        self.score = 0 
        self.total_time = 0 
        self.data_file_name = "./data.txt"
        self.high_score = -9999999999999
        
    def type_a_line( self, sentence_to_type):
        print( "type this back and then hit ENTER")
        print( sentence_to_type)
        time.sleep(1)

        tstart = time.time()

        userin = input()

        tend = time.time()

        deltat  = tend - tstart

        if( userin ==  sentence_to_type):
            print( " correct" ) 
            self.score = self.score + 1 
        else:
            print(" wrong")
        

        print( "that took" + str(deltat) + " seconds")
        print( "you are typing at " + str( (1+sentence_to_type.count(" "))*60/deltat ) + " words per min" ) 
        self.total_time = self.total_time + deltat

    def read_high_score( self ):
        with open(  self.data_file_name , 'r') as f:
            data = float(f.read() )
            return(data)
    
    def write_high_score( self):
        with open(self.data_file_name , 'w') as f:
            f.write(  str( self.score ) )
            
    
    def play_game(self):
        for a in self.list_of_sentences:
            self.type_a_line(a)
        
        self.score = self.score*50 - self.total_time
        print( "Your score was : " , str(self.score))
        self.high_score = self.read_high_score()
        print( "The current high score is : " + str(self.high_score))
        
        if( self.high_score < self.score):
            print( "NEW HIGH SCORE")
            self.write_high_score()
        else:
            pass
        
        
        
# ~ with open("test.txt" , 'w') as f:
    # ~ f.write(  str( "this is a test file" ) )

mygame = game( list_of_sentences)
# ~ mygame.write_high_score()
mygame.play_game()



