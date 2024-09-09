a=int(input("Enter first Number:\n"))
b=int(input("Enter second Number:\n"))
# Initialize maxNum with the larger of the two numbers
maxNum=max(a,b)
while(True):
    # Check if maxNum is divisible by both a and b
    if(maxNum%a==0 and maxNum%b==0):
        break
    maxNum=maxNum+1  #increment maxNum and check again

print(f"The LCM of {a} and {b} is {maxNum}")