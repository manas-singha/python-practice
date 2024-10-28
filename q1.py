#Fibonacii series upto 10 terms
num1,num2=0,1
for i in range(10):
    print(num1)
    next=num1+num2
    num1=num2
    num2=next
#Reverse a given integer number
number=int(input("enter a number:"))  
rev=0
while number>0:
    last=number%10
    rev=rev*10 +last
    number=number//10
print(rev)    


