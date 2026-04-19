a = 100
print(type(a))

a="100"
data = isinstance(a, str)
print(data)


## arithimetic operators

a = 2
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)

print(a**b)


## string + * 
## str + str is right way 
## str + INT x is wrong 

a= "Hello  "
b = "World"
c=123
# print(a+b+"   "+c)
# print(c*30)  # can only multiply str with numbers not with variable 

print(str(a)* int(c))