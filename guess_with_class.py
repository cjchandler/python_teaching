class guess:
    def __init__(self):
        self.answer = 4 
        self.n_trys = 0
        
    def check_input(self, a):
        try:
            a = int(a)
            if (a == self.answer):
                return 1
            else: 
                return 0 
        except:
            print( "numbers bro, numbers")
            return -1
        
    def level_1(self):
        print ("guess a number between 1 and 10 ")
        for b in range( 0 , self.n_trys):
            
            a = input()
            check_val = self.check_input(a)
            if (check_val == 1):
                print(" yay!")
                return 1
            elif (check_val == 0):
                print("no...")
            else: 
                pass
            
        
        print("time's up")
        return 0
        
    # ~ def level_2(self):
        # ~ print ("guess a number between 1 and 100 ")
        # ~ for b in range( 0 , self.n_trys):
            
            # ~ a = input()
            # ~ try:
                # ~ a = int(a)
                # ~ if (a == self.answer):
                    # ~ print(" yay!")
                    # ~ return 1
                # ~ else: 
                    # ~ print("no...")
            # ~ except:
                # ~ print( "numbers bro, numbers") 
        
        # ~ print("time's up")
        # ~ return 0
            
        
    
    
G = guess() 
G.level_1()
