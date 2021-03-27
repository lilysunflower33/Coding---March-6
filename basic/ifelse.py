who = input("who are you?")

if who == "dog":
    print ("bark!")
elif who == "cat":
    print("Meow!")
else:
    print("Nothing")

age = int(input("How old are you?"))
#str to convert int to string
if age < 16:
    print("need to be 16 years old!")
else:
    print("you are ok to go!")