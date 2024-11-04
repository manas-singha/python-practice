def power2(n):
    if (n==1):#base case (1)
        return 2
    smallAns=power2(n-1) #induction hypothesis (2)
    ans=2*smallAns #using 2
    return ans
print(power2(5))