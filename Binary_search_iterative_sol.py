
# coding: utf-8

# In[9]:


# recursive solution of binary search for sorted array
import math
def binary_search(A,n,x):
    low = 0
    high = n - 1
    while low <= high:
        mid = math.floor(low + (high - low)/2)
        if x == A[mid]:
            return mid
        elif x < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    else:
        return -1
    
A = [2,6,13,21,36,47,63,81,97]
x = int(input("Enter any number: "))
result = binary_search(A,len(A),x)
if result == -1:
    print("The element is not in the array")
else:
    print("The element is present at index number {}".format(result))
    
        

