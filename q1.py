#Fibonacii series upto 10 terms
num1,num2=0,1
for i in range(10):
    print(num1)
    num1,num2=num2,num1+num2
#Reverse a given integer number
number=int(input("Enter a number:"))
rev=0
while number>0:
    rev=rev*10+number%10
    number=number//10
print(rev)    


