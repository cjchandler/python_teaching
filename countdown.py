holidays = {}
holidays["christmas"] = 25
holidays["new years"] = 32
holidays["Issac's Birthday"] = 22

print( "welcome to countdown.  christmas,  new years , or Issac's Birthday") 
invar = input()
try: 
    holiday_number = holidays[invar]
except: 
    print( "not an option") 
    exit() 

print( "type the todays date (format ex dec 12)" )
instring = input()
inlist = instring.split(" " ) 

if( int( inlist[1]) > 31 ):
    print( "type a real date. Foolish user." )
    exit()


if( inlist[0] != "dec" ):
    print( " you must wait a long time until " + invar + " . Talk to me again in dec" )
    exit()
    
target_date = holiday_number 

days_left = target_date - int( inlist[1])  



if( days_left < 0 ):
    print( "you must wait a very long time until " + invar + ".") 
    exit()

    
print( "there are " + str(days_left) + " until that special day ")

