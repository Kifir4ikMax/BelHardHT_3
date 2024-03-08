def verify_first(firstname):
    while not firstname.isalpha():
        print("Invalid name, please enter again!")
        firstname = input("Enter your name: ")
    return firstname


def verify_last(lastname):
    while not lastname.isalpha():
        print("Invalid lastname, please enter again!")
        lastname = input("Enter your lastname: ")
    return lastname


def verify_digit(age):
    while not age.isdigit():
        print("Invalid age, please enter age with digits!")
        age = input("Enter your full age: ")
    return age


def lesson_3_data_types():
    firstname = verify_first(input("Enter your name: "))
    lastname = verify_last(input("Enter your lastname: "))
    age = verify_digit(input("Enter your full age: "))
    quote = f"Привет, меня зовут {lastname} {firstname}, мне {age} лет"
    print(f"{quote}\n{quote[2]}\n{quote[-2]}\n{quote[0:5]}\n{quote[0:-2]}")
    some_str = "Hello, World!"
    print(f"{some_str[0:7]}{firstname}{some_str[-1:]}")
    print(some_str.replace('World', firstname))


lesson_3_data_types()
