## * - abstict in function means it stores all data in one 

def user_info(**info):
    # print(info)
    print(info.get("name"))

user_info(name="John", age=30, city="New York")

# single abstrict / arguments use garda kunai functin use garda tyo function already def ma define vako hunu parthiyo 


data = {"name": "John", "age": 30, "city": "New York"}
print(data.items())


#enumerate - it is used to get the index of the element in a list or tuple
print("--------------------0-0-0-000---------------------------")

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
print_info(name="John", age=30, city="New York")

def print_tuple_info(*args):
    for index, value in enumerate(args):
        print(f"{index + 1 }: {value}")
        
print_tuple_info("John", 30, "New York")

print("--------------------0-0-0-000---------------------------")
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
student_info(100,82,62,95, name="John", age=30, city="New York")
        
        
print("--------------------0-0-0-000---------------------------")

