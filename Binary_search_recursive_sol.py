
# recursive solution of binary search for sorted array
import math
def binary_search(A,low,high,x):
    if low <= high:
        
        mid = math.floor(low + (high - low)/2)
        if x == A[mid]:
            return mid
        elif x < A[mid]:
            return binary_search(A,low,mid -1,x)
        else:
            return binary_search(A,mid+1,high,x)
    else:
        return -1
    
A = [2,6,13,21,36,47,63,81,97]
x = int(input("Enter any number: "))
result = binary_search(A,0,len(A)-1,x)
if result == -1:
    print("The element is not in the array")
else:
    print("The element is present at index number {}".format(result))
    
        

