def greet_person(name, greeting="Hello"):
    message = f"{greeting},{name}"
    return message

default_greeting = greet_person("Alice")
print(default_greeting)

custom_greeting = greet_person("Alice","Hi")
print(custom_greeting)


def shume_nr_qift():
    total =0
    for number in range(1,10):
        if number % 2 ==0:
            total = total + number
    return total


print(shume_nr_qift())