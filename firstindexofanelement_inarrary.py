def FirstIndex(l1,x):
    if (len(l1)==0):
        return -1
    if (l1[0]==x):
        return 0
    ansfromRecursion=FirstIndex(l1[1:],x)
    if ansfromRecursion==-1:
        return  ansfromRecursion
    else:
        return ansfromRecursion +1
    
print(FirstIndex([3,2,5,2,8,2,1],4))    