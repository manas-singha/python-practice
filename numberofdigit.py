def NumberofDigits(n):
    if (n>=1 and n<=9):
        return 1
    elif (n==0):
        return 1
    smallNumber=int(n/10)
    smallAns=NumberofDigits(smallNumber)
    ans=1+smallAns
    return ans
print(NumberofDigits(123))
print(NumberofDigits(8))