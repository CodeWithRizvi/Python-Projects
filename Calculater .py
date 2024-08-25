first= input("Enter first number: ")
operator=input("Enter operator(+,-,*,/,%): ")
second= input("Enter second number: ")
# Convert the input values from strings to integers
first=int(first)
second=int(second)

# Check which operator was entered and perform the corresponding operation
if operator=="+":
    print(first+second)
elif operator=="-":
    print(first-second)
elif operator=="*":
    print(first*second)
elif operator=="/":
    print(first/second)
elif operator=="%":
    print(first%second)
elif operator=="//":
    print(first//second)
else:
    # If the operator is not recognized, print an error message
    print("Please try again later")