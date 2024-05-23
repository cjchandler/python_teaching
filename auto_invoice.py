#make and send coding invoices, pure text

import time
from datetime import date


def make_preamble_string( customer_name , customer_email):
    
    date_today =  date.today()

    header_dict={}
    header_dict["company name"] = "Sun Aquasystems Ltd"
    header_dict["HST number"] = "HST: " + str(794893537)
    header_dict["name of customer"] = "Bill to: " + customer_name
    header_dict["email of customer"] ="         " + customer_email
    header_dict["date"] = str(date_today)
    
    out_string = ""
    for a in header_dict.keys():
        out_string = out_string + header_dict[a] + " \n"
        
    return out_string





def make_labor_cost_string( datestring):
    hourly_rate = 15.5
    hours_per_event  = 1.5
    rate_per_event = hourly_rate*hours_per_event

    total_bill_no_tax = len(datestring)*rate_per_event
    tax = 0.15*total_bill_no_tax
    total_with_tax =  tax + total_bill_no_tax
    
    out_string = "Hourly rate is "+ str(hourly_rate) + " CAD per hour \n \n"
    out_string = out_string + "date".ljust(19) +   "hours \n"
    
    for a in datestring: 
        temp = a.ljust(19)
        out_string = out_string + temp + " " + str(hours_per_event).ljust(4) + " \n"

    out_string = out_string + " \n"

    out_string = out_string + "Labour cost: " + str(round(total_bill_no_tax, 2)) + " \n"
    out_string = out_string + "HST        : " + str(round(tax, 2)) + " \n"
    out_string = out_string + "Total      : " + str(round(total_with_tax, 2)) + " \n"
    
    return out_string

dates =  [  "5 apr 2024" , "19 apr 2024" , "26 apr 2024"    ]

print( make_preamble_string( "Sung-sik Kim (902-401-2598)" , "kss7489@gmail.com" ) )
print( make_labor_cost_string(dates))

print() 
print() 
print() 
print( make_preamble_string( "Juyeon Lee " , "leejuyeon10300509@gmail.com" ) )
print( make_labor_cost_string(dates))




