#dry tomato 
print( "type in teh we mass of the tomato and tray")
wet_g = int(input()) 
print(" type the mass of teh tray alone" ) 
tray_g = int(input())

print("type the dry tomatoe mass and tray")
dry_g = int(input())

percent = ((dry_g-tray_g*1.0)/(wet_g*1.0 -tray_g))*100.0

print( percent)


