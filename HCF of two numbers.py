num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
# Determine the smaller of the two numbers to limit the range of the loop
if num2>num1:
    nm=num1
else:
    nm=num2
# Loop through numbers from 1 to nm (inclusive) to find common factors
for i in range(1, nm+1):
    # Check if i is a divisor of both num1 and num2
    if num1%i==0 and num2%i==0:
        HCF=i   # Update HCF to the current divisor
print(f"The HCF/GCF of these two number is {HCF}")