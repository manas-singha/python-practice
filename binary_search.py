def binary_search(arr,target):
    size=len(arr)

    start=0
    end=size -1
    while (start<=end):
        mid=(start+end)//2
        if (arr[mid]==target):
            return mid 
        elif(arr[mid]>target):
            end=mid -1
        elif(arr[mid]<target):
            start= mid +1    
    return -1       


arr=[10,23,35,45,50,70,85]
target=35
result=binary_search(arr,target)
print(result)