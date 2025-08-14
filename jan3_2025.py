#jan 3 2025

print(" hey I hear you like zeros, how many do you want?") 
a = input() 
num_zeros = int(a) 

incrementqqw = 0.001
z = "0" 
d = "." 
string_increment = z+ d 
for a in range( 0 , num_zeros-1):
    string_increment = string_increment + z 
    
string_increment = string_increment + "1" 
print( string_increment)

incrementqqw = float( string_increment)


t = 0 
while t <= 1:
     print( t) 
     t = t + incrementqqw


# ~ print("Hey what do you like to count by? " )
# ~ a = input() 
# ~ i = float(a) 

# ~ t = 0 
# ~ while t <= 1:
     # ~ print( t) 
     # ~ t = t + i
 
