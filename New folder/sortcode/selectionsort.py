def selectionsort(arr):
    for i in range(1,len(arr)):
        temp=arr[i]
        count=0
        while arr[i]<arr[i-1-count] and (i-count-1)>=0:
            
            arr[i-count]=arr[i-1-count]
            count+=1
        arr[i-count]=temp
    
arr=[4,6,9,8,38,98,97]
selectionsort(arr)
print(arr)