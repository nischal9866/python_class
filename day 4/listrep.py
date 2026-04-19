# a = [1,2,3,4,5,6]
# print(type(a))
# print(a[0])

# print(len(a))

# a = [1,2,3,4,5]
# print((len(a))-1 )


# ## slicing 
# name = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris','Ihsan']
# print(name[1:5])
# print(name[1:])
# print(name[:6])
# print(name[:])

# name = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris','Ihsan']
 
# #append
# name.append("krish")
# name.append([1,2,3])
 
 
# # insert
# name.insert(2,"insert")
# name.insert(20,"should be error")
# print(name)
 
 
# # extend
# a = [1,2]
# b = [3,4]
# a.extend(b)
# print(a)
# print(b)
# b.extend(a)
# print(b)
# a.extend(b)
# print(a)
 
# # concat
# print("......."*3)
# a = [1,2]
# b = [3,4]
 
# c = a+b
# print(c)
# print(a, b)
 
 
# data = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris','Ihsan']
# del data[1]
# print(data)
 
# # pop
# deleted_name = data.pop()
# print(data)
# print(deleted_name)
 
# # remove
# data.remove("Haris")
# data.remove("Haris")
 
 
# # clear
# data.clear()
# print(data)
 
 
# # sort
# teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil','Haris', 'Ihsan']
# teachers.sort(reverse=True)
# print(teachers)
 
# data = ['Nasir', 'Irfan', 'insert', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris', 'Ihsan', 'krish', [1, 2, 3], 'should be error']
# print(data[10][1])
# list_data =data[10]
# print(list_data[1])

numbers = [12, 45, 7, 89, 23, 56, 3, 78]

numbers.sort()

min_val = numbers[0]
max_val = numbers[-1]

print("Minimum:", min_val)
print("Maximum:", max_val)