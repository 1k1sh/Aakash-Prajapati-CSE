#Given an array, rotate the array by one position in clock-wise direction.
def rotate( arr, n):
    
    a=arr[n-1]
    
    for i in range(n,1,-1):
           arr[i-1]=arr[i-2]
    arr[0]=a


#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1