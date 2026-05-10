print("Working on new feature")

def add(a, b):
    return a + b

print(add(5, 10))

# Another change

print("Incorrect code")

def divide(a, b):
    return a / 0

# Fixing the incorrect code

def divide(a, b):
    return a / b

print(divide(10, 2))