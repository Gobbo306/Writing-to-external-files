#------------------------------------------------
#Dylan Friesen
#Writing to external files
#Friday October 18, 2019
#------------------------------------------------

#---------------Functions------------------------

def writing_to(): #importing the file so that it can be used
    file = open('Dangerous Randall.txt', 'w') 
    print("the file is being opened") #showing the user that it is being opened
    choice1 = input("What do you want to put into the file?")
    file.write(choice1) #putting whatever it was that
    print("The file is being closed")
    file.close()
    
def appending_to(): #used to add to the file, without removing the text that was added with the previous action
    file = open('Dangerous Randall.txt', 'a')
    print("file is being opened")
    choice2 = input("What are you adding to the file?")
    file.write(choice2)
    print("the file is being closed")
    file.close()
    
def character_creation(): #used to create details of user's character.
    print("The file is being opened")
    name = input("What is the name of your character?")
    race = input("What race are you?")
    gender = input("What gender are you?")
    file = open('character creation.txt', 'w')
    file.write("User=") #using equals to clear up the writing a bit, stop it from being so clumped
    file.write(name + ",")
    file.write("Race=")
    file.write(race + ",")
    file.write("Gender=")
    file.write(gender + ",")
    print("The file is being closed")
    file.close()

#-----------------------Main---------------------

def main(): #putting all them defs to use
    writing_to()
    appending_to()
    character_creation()
    
main() #its time