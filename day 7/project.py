import random

data = ["r","p","s"]
computer = random.choice(data)
print(computer)
while True:
    user_num = input("Guess the r/p/s: ").lower()
    if user_num == computer:
        print("draw")
    elif (user_num == "r" and computer == "s") or (user_num == "p" and computer == "r") or (user_num == "s" and computer == "p"):
        print("You win")
    else:
        print("You lose")

