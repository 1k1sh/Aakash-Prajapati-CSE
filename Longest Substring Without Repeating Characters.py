class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st=[]
        count=0
        maxi=0
        for i in range(len(s)):
            if s[i] not in st:
                st.append(s[i])
                count+=1
                maxi=max(maxi,count)
            elif s[i] in st:
                ind=st.index(s[i])
               
                st=st[ind+1:]
                st.append(s[i])
                count=len(st)
                
                
        return maxi