import random
count = 0
userinput=input("Enter the number between 1 to 6 : ")
while count < 1:
    num = random.randint(1, 6)

    if num == userinput:
        print ("You win !!! ")
        break
    count += 1
else:
    print ("Sorry, you lose!")
    print("You enter "+ str(userinput))
    print("And number was "+ str(num))

