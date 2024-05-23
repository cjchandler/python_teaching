# importing yagmail and its packages 
import yagmail 
  
# initiating connection with SMTP server 
password = input()
yag = yagmail.SMTP("carljosephchandler@gmail.com",  ) 
  
# Adding multiple recipents name in "to" argument 
yag.send("cjchandl@ualberta.ca" , "Subject Of Mail","Content Of Mail")
