from random import*
from PIL import Image #import package Image from Pillow library
image1=Image.open('youre-goddamn-right.jpeg') #Make sur the jpeg is on YOUR DESKTOP !!

h = randint(1,9)
guess = 0 #initialize knowing that h goes from 1 to 9
count = 0

while guess!=h and guess != "exit":
   
    guess = input("Guess a number between 1 and 9 : ")
    
    if guess == "exit":
        print("Ok chill buddy")
        break
    
    guess = int(guess)
    count+=1
    
    if guess<h:
        print("Too low, try again")
    elif guess>h:
        print("Too high, try again")
    else:
        print("You're god damn right, it tooks you "+str(count)+" tries !")
        image1.show()
