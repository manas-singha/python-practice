def fibonacii(n):
    if (n==0):
        return 1
    if (n==1):
        return 1
    last=fibonacii(n-1)
    secondlast=fibonacii(n-2)
    ans=last+secondlast
    return ans
print(fibonacii(4))