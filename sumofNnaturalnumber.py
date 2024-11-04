import sys
sys.setrecursionlimit(5000)

def sumofNumbersTillN(n):
    if (n==1):
        return 1 #Base case
    smallAns=sumofNumbersTillN(n-1)
    ans=n+smallAns
    return ans
print(sumofNumbersTillN(1000))