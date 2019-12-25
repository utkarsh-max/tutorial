import random
n = random.randint(1, 99)
print(n)
print("You just have 5 chance")
chance=0
guess = int(input("Enter an integer from 1 to 99: "))
while n != guess:
    while chance <= 5:
        #chance = chance + 1
        if guess < n:

            print("guess is low")

            guess = int(input("Enter an integer from 1 to 99: "))
            chance = chance + 1
        elif guess > n:

            print("guess is high")

            guess = int(input("Enter an integer from 1 to 99: "))
            chance = chance + 1

        else:
            print("You guessed it")
            break

    print("Your chance is over")
    break



# break




'''else:
    print(guess)'''








