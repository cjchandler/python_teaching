gravity = 9.81
window_diameter_m  = 0.2

pi = 3.14 
window_radius = window_diameter_m/2
window_area_m2 = pi*window_radius*window_radius
inside_spaceship_pressure_Pa = 101000
##f = ma 
##m = f/a 

total_window_force = inside_spaceship_pressure_Pa*window_area_m2

window_mass_to_support = total_window_force/gravity

print( " the window should be able to support this many kg:")
print( window_mass_to_support )

###


x = 9 

#x + y =10
y = 10 -x

print( y)
