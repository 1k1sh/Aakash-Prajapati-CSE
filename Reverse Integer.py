class Solution:
    def reverse(self, x: int) -> int:
        lis=[]
        
        if x<0:
            y=abs(x)
        else:
            y=x
        if y==0:
            return 0
        
        while y!=0:
            temp1=y%10
            y=y//10
            lis.append(temp1)
            
        ans="".join(map(str,lis))
        if int(ans)<=-2**31 or int(ans)>=(2**31)-1:
            return 0
        if x<0:
            return -abs(int(ans))
        return (int(ans))