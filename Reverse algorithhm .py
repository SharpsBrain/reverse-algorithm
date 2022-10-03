#!/usr/bin/env python
# coding: utf-8

# In[4]:


#function to revers arr[] from index start-end:
def reverseArray(arr,start,end):
    while(start<end):
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start+=1
        end=end-1
#function to left rotate arr[] of size n by d
def leftRotate(arr,d):
    n=len(arr)
    reverseArray(arr,0,d-1)
    reverseArray(arr,d,n-1)
    reverseArray(arr,0,n-1)
#function to print the array
def printArray(arr):
    for i in range(0,len(arr)):
        print(arr[i])
#driver function to test above functions
arr=[1,2,3,4,5,6,7,8,9,10]
leftRotate(arr,5)#rotate array by 2
printArray(arr)


# In[ ]:




