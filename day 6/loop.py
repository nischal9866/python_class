#for loop - 
print("________loop__________________")

# for i in [1,2,3,4,5,6,7,2,35,6,65,343,34,43,43,34]:
#     print(i)
    
# for j in ["broadway","haru"]:
#     print(j)
    
user_info = {
    "city":"dang",
    "number":90,
    "name":"Nischal"
}

# for i in user_info:
#     print(i,user_info[i])


# for j in range(1,20,5):    #the meaning we put last value 5 is it increase by 5 increment
#     print(j)

# print("__next__")

# for i in range(1,10,-2):
#     print(i)
    
# for i in range(1,10,1):
#     if i%2==0:
#         print(i)
        
print("----nested forloop------")
# for x in [1,2,3]:
#     for y in [4,5,6,7]:
#         print(x,y)

#break,continue


#break = if i chose some value and break it only goes until that value came and loop stops 
#continue = other values continues to loop except that one value which we chose to use continue 
# for a in range(1,10,1):
#     if a ==5:
#         continue
#     print(a)
    
my_list= [
1, "a", 2, "b", 3, "c", 4, "d", 5, "e",
6, "f", 7, "g", 8, "h", 9, "i", 10, "j"
]

for i in my_list:
    if isinstance(i, str):   
        continue
    print(i)
    