'''
def say_hello():
    return "Hello"
    
    print(say_hello)
    
def say_hello_user(name):
    print("Hello " + name)

name = "Jafet"    
say_hello_user(name)

def user_year_old(actual_year, born_year):
    years_old =actual_year - born_year
    return years_old

print(user_year_old(2021, 1998))

'''

def add_number(number_one, number_two):
    added_numbers = number_one + number_two
    return added_numbers

print(add_number(20, 25))


def multiplication(number_1, number_2):
    result = number_1 * number_2
    return result

print (multiplication(10, 10))