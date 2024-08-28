def a_(n):
    if(n==1):
        return 1
    else:
        return n* a_(n-1)
print(a_(5))




             ##
n=int(input("Enter a number:"))
product=1
for i in range(1, n+1):
    product=product*i

print(f"The factorial of {n} is {product}")