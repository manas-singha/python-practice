def sumArray(l1):
    if len(l1)==0:
        return 0
    sumofleftoverarray=sumArray(l1[1:])
    ans=sumofleftoverarray+l1[0]
    return ans
print(sumArray([1,2,3,4]))