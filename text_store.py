c = 7 
b = 9 
x = 5

name = "carl"
hello = "hello"
space  = " "  
print( hello + space+ name) 


inventory_dict = {}
inventory_dict[ "goat" ] = 100 
inventory_dict[ "cat" ] = 0 
inventory_dict[ "dog" ] = 1000 
inventory_dict[ "squirrel" ] = 5.50
inventory_dict[ "knife" ] = 15.99
inventory_dict[ "car" ] = 25900

 

def get_price_with_tax( base_price ):
    price_tax_included = base_price + base_price*0.15
    return price_tax_included

def print_dict_of_items_and_prices( inventory_dict_in ):
    print("Here are the items and prices for the things in our store")
    for item_name in inventory_dict_in.keys():
        print( " ", item_name , inventory_dict_in[item_name] , "CAD" )

####your job: make a new fuction that uses these functions to print out the items for sale, and what will be the price with tax 




print( "price_for_goat_with_tax" , get_price_with_tax(100) )
print_dict_of_items_and_prices( inventory_dict)


print( get_price_with_tax(100))
print( get_price_with_tax(123))
print( get_price_with_tax(103))
print( get_price_with_tax(13))
print( get_price_with_tax(1))


myFancyVariable = 9 

exit()


###new program, make a interactive store 
def add_item( ):
    print( "type the name of the item" ) 
    name = input()
    print( "type the base price" ) 
    string_price = input()
    float_price = float( string_price)
    inventory_dict[name] = float_price
    
    print( "all done" )


def buy_item( item_name , inventory_dict):
    #do some stuff here , make sure you tell them how much it will be with tax included 
    return 

while(True):

    print( "hello! welcome to Gary's store. If you want to buy, type the name of what you want.")
    print( "If you want to see a list of items and prices, type list") 
    print( "If you want add an item to sell type, shopkeeper")

    string_in = input()

    if( string_in == "list" ):
        print_dict_of_items_and_prices( inventory_dict)
    
    if( string_in == "shopkeeper"):
        add_item( )
        
    ###now your job is to make some code to tell the user how much the item will cost with tax
        











# ~ def tax_included( a):
    # ~ return a*0.15 + a
    
# ~ def sale( b) :
    # ~ return b/2 
    
# ~ def sale_with_taxes( c):
    # ~ sale_price =sale(c)
    # ~ sale_and_tax_added = tax_included(sale_price)
    # ~ return sale_and_tax_added
    
# ~ print( sale_with_taxes(30))




# ~ import time
# ~ from datetime import date

# ~ header_list = []
# ~ header_list.append( "company name")
# ~ header_list.append( "date")
# ~ header_list.append( "HST number")
# ~ header_list.append( "name of customer")
# ~ header_list.append( "email of customer")

# ~ header_values= []
# ~ header_values.append("Sun Aquasystems Ltd")
# ~ date_today =  date.today()
print(date_today)

# ~ header_values.append( str(date_today) )
# ~ header_values.append( 404)
# ~ header_values.append( "bob jones")
# ~ header_values.append("bob@jones.com")


# ~ header_dict={}
# ~ header_dict["company name"] = "Sun Aquasystems Ltd"
# ~ header_dict["HST number"] = 404
# ~ header_dict["name of customer"] = "bob jones"
# ~ header_dict["email of customer"] = "bob@jones.com"
# ~ header_dict["date"] = str(date_today)


# ~ for x in header_dict:
    # ~ print(x ,":",  header_dict[x])


# ~ def f(a):
    # ~ return 3*a 

# ~ def l( a, b , d):
    # ~ return [a,b,d] 

# ~ def p( A , B , C):
    # ~ return l( f(A) , f(B) , f(C) )

# ~ class working_period:
    # ~ def __init__(self , n_hours_worked):
        # ~ self.hours = n_hours_worked
        # ~ self.minutes = 0
        # ~ self.date = "no data assigned"
        # ~ self.billing_total = 0
        # ~ self.billing_rate_per_hour=0
         
    # ~ def change_billing_rate( self , new_rate):
        # ~ self.billing_rate_per_hour = new_rate 
         
    # ~ def calculate_total( self ):
        # ~ self.billing_total = self.billing_rate_per_hour*( self.hours + self.minutes/60.0 )
        
    # ~ def calculate_total_with_tax(self):
        # ~ return self.calculate_total()*1.15
    
        
# ~ c = 9
# ~ print( c) 
# ~ print( f(c))

# ~ print( p( 2,4,8) )

# ~ G = working_period(3.5)
# ~ G.change_billing_rate(28)
# ~ G.calculate_total()
# ~ print( G.billing_total )


