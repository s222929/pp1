import mymath

the_number = mymath.generate_number()
user_number = mymath.read_number()
while user_number != the_number:
    user_number = mymath.read_number()

print("You won!")