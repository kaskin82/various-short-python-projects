import random #chooses a random number
min = 1 #this means the minimum number possible is 1
max = 20 # this sets the amx number rollable to be 20

roll_again = "yes" #this is the variable that kicks off the rest of the script

while roll_again == "yes" or roll_again == "y": #checks what roll again is set to
    print "alright lets see if you get lucky"
    print "you rolled..." #this is just printed flavor text
    print random.randint(min, max)
    print random.randint(min, max) #this chooses a random integer betweeen the assigned min and max values in this case between 1 and 20

    roll_again = raw_input("roll the dices again?") #allows user to set the value for roll again by text input yes or y will roll again.
    
    
