'''
Created on Oct 11, 2015

@author: DhruvGala

The following code mimics the rolling dice concept.
It asks the user for the faces of the dice and then keeps on rolling the dice 
until the user demands to stop it.
It is a basic implementation of random integer generator function provided by Python.
'''
from pip._vendor.distlib.compat import raw_input
from random import randint


'''
The following method implements the actual logic of rolling the dice and showing the face up number.
'''
def rollTheDice(numberOfFaces):
    keepRolling = True
    
    while(keepRolling):
        faceUp = randint(1,numberOfFaces)
        print("Dice rolled to {}".format(faceUp))
        
        choice = raw_input("Do you want to roll the dice:(y/n) ")
        if choice == "n":
            keepRolling = False
        

'''
this method takes the initial input of number of faces on the dice from the user.
'''    
def takeInput():
    faces = raw_input("Enter the sides of the dice: ")
    
    try:
        n = int(faces)
    except:
        print("Invalid input")
        
    return n

'''
main function
'''
def main():
    numberOfFaaces = takeInput()
    rollTheDice(numberOfFaaces)
    
#call the main method        
if __name__ == "__main__": main()        