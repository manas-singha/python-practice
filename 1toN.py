def print1toN(n):
    if (n<=0):
        return
    print1toN(n-1)   #use head recursion here
    print(n)
print1toN(5)    


#print Nto 1
def print1toN(n):
    if (n<=0):
        return
    print(n)
    print1toN(n-1)   #use tail recursion here
print1toN(5)
