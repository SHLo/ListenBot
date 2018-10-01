import os.path
import random

def talk_jokes():
    # read the postive and negative corpus
    joke = ['Can a kangaroo jump higher than a house?  Of course, a house doesn’t jump at all.', 'What is orange and sounds like a parrot? A carrot.','Where do pencils spend their vacations?  In Pencilvania.','Why did the physics teacher break up with the biology teacher? There was no chemistry.', 'A: I have a doctor’s appointment today but I really don’t want to go… B: Just call in sick then.']
    again = False
    print ("You look bad today, Let me say a joke to you")
    response = input("Do you want to hear? (Y/N) ")
    if(response == "Y"):
        while (response == "Y"):
            if (again == True):
                print ("You look bad today, Let me say one more joke to you")
            print(random.choice(joke))
            response = input("Do you still feel bad? (Y/N) ")
            if (response == "Y"):
                again = True

    else:
        print("OK. Hope you get well soon")
