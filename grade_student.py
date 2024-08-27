marks = int(input("Enter your number: "))

if(marks<=100 and marks>=90):
    grade = "Ex"
elif(marks<=90 and marks>=80):
    grade = "Ex"
elif(marks<=80 and marks>=70):
    grade = "Ex"
elif(marks<=70 and marks>=60):
    grade = "Ex"
elif(marks<=60 and marks>=50):
    grade = "Ex"
elif(marks<50):
    grade = "F"
    
print("Your grade is :", grade)