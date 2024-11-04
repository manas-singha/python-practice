a=[0,1,2,4,5,8,9]
target=0
# size=len(a)
# def linear_search(a,target):
#     for i in range(size):
#         if a[i]==target:
#             return True
#     return False    
# print(linear_search(a,target))



def binary_search(a,target):
    start=0
    end=len(a)-1
    
    while (start<=end):
        mid=(start+end)//2
        if a[mid]==target:
            return mid
        elif a[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return False
print(binary_search(a,target))

