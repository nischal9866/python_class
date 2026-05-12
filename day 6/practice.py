# i = "*"

# while len(i) <= 5:
#     print(i)
#     i = i +"*"
    
# j = "*****"
# while len(j)>0:
#     print(j)
#     j = j[:-1]

# sum = 0 
# n =6
# for i in range(1,n+1):
#     sum+=i
#     print(sum)

# n=2
# for i in range(1,10):
#     print(n*i)
    
    
import random
random_num = random.randint(0,20)
print(random_num)
count = 0
plays = 1
 
while True:
    count += 1
    user_num = int(input("Guess the number: "))
    if user_num == random_num:
        print(f"Number Guess Successfully, You guessed in {count} trials")
        x=input("Do you want to play again? (y/n): ")
        if x.lower() == 'y':
            random_num = random.randint(0,20)
            print(random_num)
            count = 0
            plays = plays + 1
        else:
            print(f"Thanks for playing, you have play this game {plays} times  ")
            break
       
    else:
        if user_num > random_num:
            print("Too High")
        else:
            print("Too Low")
