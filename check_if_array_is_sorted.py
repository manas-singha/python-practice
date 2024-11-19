def checkSorted(l1):  #using Recursion
    if(len(l1)==0 or len(l1)==1):
        return True
    ans=checkSorted(l1[1:])
    if (l1[0] < l1[1]):
        return ans    #here you can write ans/True
    else:
        return False
print(checkSorted([2,5,7,9,10]))    