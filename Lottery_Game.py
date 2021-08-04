#import random library
import random

#specify range of lotter number
lottery = random.randint(1,500)

print("You have only one chance to examine your luck \n\t\t\tALL THE BEST")

#let the user select the number
number = int(input("Enter a Number from 1 - 500 : "))

#using conditional statement to check weather individual won or not 
if number==lottery:
    print("Congratulations ! You won Audi A7")

else:
    print("\nBetter Luck Next time")

print("\t\t\tThanks for Participating")    
    
 
