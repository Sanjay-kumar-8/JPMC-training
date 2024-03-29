from random import randint

num=randint(1,100)
n=5
for i in range(n,1,-1):
    c=int(input("Guess the number:"))
    if c==num:
        print("You Won")
        break
    elif c>num:
        print("Guessed number is greater than the actual number")
    else:
        print("Guessed number is less than the actual number")
else:
    print("You lost the game")
