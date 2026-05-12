import random


x = random.randint(0,5)
count = 0

while True:
    count = count +1
    user = input("guess a number")
    if user == str(x):
        print(f"Your guess was right in {count} times")
        
        break
    else:
        print("try again")




