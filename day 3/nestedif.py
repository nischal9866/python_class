# marks= int(input("Enter marks"))

# if marks<0 or marks>100:
#     print("wrong input")
# elif marks >=90:
#     if marks == 100:
#         print("perfect 100")
#     print("A")


# using if else condition inside if else itself 
##note : the main priority will be focused on parent if else and only after inside if else condition works 
    
age = 19
country = "nepal"
code = "Nepals"
if age > 18:
    if country == code.lower():
        print("eligible for licence ")
    else:
        print("not eligible forlicence ")
else:
    print("minor")
    
    
# using not operator     
is_raining = False

if not(is_raining):
    print("you can go outside")
    
    
## using if else in single line 

gender = "M"

data = "Male" if gender == "M" else "Female"
print(data)


# x = int(input("enter any number"))

# if x > 0:
#     if (x%2)==0:
#         print("even")
#     else:
#         print("odd")
# else:
#     print("negative")

age = int(input("enter your age "))
day=int(input("today's day"))

if age<=18:
    print("child")
    