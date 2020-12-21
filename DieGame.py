import random
die=range(6)
pop=random.choice(die)
num=int(input("Please enter your guess\n"))
if(pop==num):
    print("Your guess is right!\nYou won!")
elif(num>=7):
    print("Please enter a valid input")
else:
    print("Your guess was ",num)
    print("Original choice is ",pop)
    print("Your guess is wrong ! Try again..!!")
