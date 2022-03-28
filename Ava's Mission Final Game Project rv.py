#Roxana Villagomez
#Ava's Mission (Final Game)

#My space game is about a girl who has been working as an intern at NASA for the past six months, training with the smartest scientist professionals.
#On her last day as an intern, she was excited to request a permanent job, but something went wrong on that day.
#There is a comet heading towards earth, and we don't know its impact. We don't know what will be damaged, but NASA has decided to send a group of astronauts to understand the situation better.

#Chapter 1

import random

print("Hello Ava's Team and Welcome!")

name = input('What is your name?')
print('Hi, ' +name)

def Chapter1():
    print("As Ava walks into the concealed lot, there are three giant rooms and while the safety team and observers are behind a room looking through a clear glass taking notes. This mission is in your hands, are you willing to sacrifice your life to save our earth planet?")
    action = input("Enter Yes Im ready or Ugh I changed my mind? ")

    if (action == "Yes Im ready"):
        print("GREAT! Lets get you ready for the your first test in which we're sure you will do amazing!.")
        Chapter2()
    else:
        print("Ugh I changed my mind?")
        print("No worries, we understand you are not ready.")
        print("Game Over!")
        Chapter1()

   
##Chapter 2 First Task
#Ava is standing still waiting on instructions, waiting for the team to say “3, 2, 1, GO!”
#She is carefully staring to each box trying to figure out what items are in them and what
#she needs to do.

        
def Chapter2():

    print('Chapter 2: Ava needs to assemble her spacesuit therefore she must know exactly what she will need.')
    print("In each room, there are items that you will need to pick carefully, your going to space and not a vacation to mexico")
    print('Which box has the right space gear you need to be protected up in space? In Box 1 a Bathing suit with a pair of sandels and sunglasses since your able to get a tan or Box 2 that has helmet, spaceboots, gloves, oxygentank or Box 3 that has paperclips with papertowels and a notebook to draw pictures')
    print('Which box is best for your spacesuit?')
    action = input("Box 1 or Box 2 or Box 3? ")


    if (action == "Box 1"):
        print("Wrong! Remember, this is NOT a vacation.")
        print("Failed the first test, try again!")
    
        Chapter1()

    if (action == "Box 2"):

        print("Yes,correct, these things are important, well done, easy breezy lemon squeezy.")
        print("You PASS! Level up and get ready, your going onto your next test!")
        print("Welcome to Chapter 3")

        Chapter3()

    else:
            print("You picked the wrong box, which makes us wonder you might not be ready for this, try again!")
            print("Game Over Sorry")
            Chapter1()

    if (action == "Box 3"):
        print("Not even close!")
        print("Game over")

        Chapter1()



#chapter 3
#after the second test, the player must complete the next task
#player must match the shape and color
#circle is green, square is orange and triangle is yellow




def Chapter3():
    print('For this test, you must match the color and shapes to the following objects, see each color and object below')

    print("Triangle is color blue.")
    print("Square is color red.")
    print("And Circle is color yellow.")
    print("This test is very critical and important, hence why you only get one shot, think about and pick the correct color for the following question, what colot is the square object?")

    action = input("blue or red or yellow? ")
    print(action)

    if (action == "blue"):
        print("NOOOOOOO! try again, re-read again.")

        Chapter3()


    if (action == "red"):
        print("Awesome, red is correct, we can now move you to the next level in Chapter 4, get a move on!")

        Chapter4() 
    else:
            print("You picked the wrong box, which makes us wonder you might not be ready for this, try again!")
            print("Game Over Sorry")
            Chapter1()

    if (action == "yellow"):
        print("Sorry you had one shot on this, re-read again when you start over!")
        print("Game over")

        Chapter1()

#Chapter 4

#Random items will pop up and player must figure out what is
#needed when using weapons, rather its living or non-living things        

def Chapter4():

    print("Chapter 4:Where your going to learn how to shoot to killBeing in space will come with lots of unexpected surprises therefore you will need to know how to use a gun, but dont worry, we will train youYou will need to be quick in choosing the right action, rather you shoot or hold your fire, got it? If a moving spider looking creature was coming towards you, what will you do. ")
    action = input("Enter shoot2kill or holdfire? ")

    if (action == "shoot2kill"):
        print("Perfect! any type of creature or alien looking encounters we cant be too carefule so you will need to shoot to kill.")
        print("Great, you are ready for the final chapter")
        Chapter5()
        
    else:
        print("holdfire")
        print("Why would you hold fire if we dont know what that thing is? Your life matters to us, therefore better be safe than sorry, lets go again.")
        print("Try again!")
        Chapter4()

#Chapter 5

def Chapter5():
    print("Chapter 5: Congrats for making thus far, you are one smart cookie")
    print("Went through training and now you and the team are getting ready for impact, its been decided that by breaking the comet smaller will impact less and cause or harm earth less therefore breaking it down it must be done")
    print("You gather the equipment and build the protected shield, all were waiting for is preparing for impact before we shoot at it, but we are not sure what will happen to us, but were willing to risk it!")
    print("Its all about having faith, how confident are you that we will make it alive and safe? We're going to make it LIVE or It was a honor working with everyone and DIE?")
    print("Enter live or die")


    if (action == "live"):
        print("Thats the spirit, were going to make it and go home")
        print("You are a true hero")
        print("You are now done with this game and thanks for playing")

    else:
        print("Well thanks for helping and people will remember you as a true hero that help and save earth")

    if (action == "die"):
        print("Thanks for being honest and it was an honor having you in this mission")
        print("Game Over") 

Chapter1()
    
#The End.
