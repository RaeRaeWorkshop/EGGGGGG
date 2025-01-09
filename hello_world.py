# Just printing out a basic string variable
#spring1 = "hello" #This is a string
#print(spring1) #This is a print command
#print(type(spring1))
#print("Hello World")

#value1 = 3
#value1 = value1 + 5
#value1 = value1 / 2
#value1 = int(value1)
#print(type(value1))
#print(value1)

#Working with integers and strings
#value1 = 6
#value2 = 3
#value3 = value1 + value2
#print("the first value is: " + str(value1))
#print("the second value is: " + str(value2))
#print("the total value is: " + str(value3))

#Replace character in string
#string = "A is the best letter"
#k_string = string.replace("A","M")
#print(k_string)

#Replace multiple characters in string
#wrong_favorite_person = "Adam"
#favorite_person = "Molly"
#string = wrong_favorite_person + " is the best... Adam didn't you know?"
#k_string = string.replace(wrong_favorite_person, favorite_person, 1)
#print(k_string)

#Lets make an if statment
#value1 = 6
#if value1 > 8 or value1 < 100:
#    print("We have a good number")
#else:
#    print("The number SUCKS")

#If statement with strings
string1 = "Ashley is the coolest"
if "Adam" or "Ashley" in string1:
    print("than it is lying")
elif "Molly" in string1:
    print("YOU ARE RIGHT!!")
elif "Jake" in string1:
    print("he is my fave")
else:
    print("Don't know the person")