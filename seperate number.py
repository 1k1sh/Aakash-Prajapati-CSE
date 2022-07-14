#Given an unsorted array arr[] of size N having both negative and positive integers. The task is place all negative element at the end of array without changing the order of positive element and negative element.
class Solution:
    def segregateElements(self, arr, n):
        pt,nt=0,0
        ar=[]
        for i in range(n):
            if arr[pt]>=0:
                ar.append(arr[pt])
                
                pt+=1
            else:
                pt+=1
        for i in range(n):
            if arr[nt]<0:
                ar.append(arr[nt])
                nt+=1
            else:
                nt+=1
        arr.clear()
        for i in range(n):
            arr.append(ar[i])
 