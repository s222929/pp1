from re import X


x = int(input("Enter a first number: "))
y = int(input("Enter a second number: "))
if x>0 and y>0 or x>0 and y<0 or x<0 and y>0:
    print("At least one of the numbers is positive")
else:
    print("Numbers are negative")
