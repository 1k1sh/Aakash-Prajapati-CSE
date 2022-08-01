class Solution:
    def isValid(self, s: str) -> bool:
        dicts={"(":")","{":"}","[":"]"}
        st=[]
        for i in s:
            if i=="(":
                st.append(i)
            elif i==")":
                if len(st)!=0 and i==dicts[st[-1]]:
                    st.pop()
                else:
                    return False
                
            elif i=="{":
                st.append(i)
            elif i=="}":
                if len(st)!=0 and i==dicts[st[-1]]:
                    st.pop()
                else:
                    return False
            elif i=="[":
                st.append(i)
            elif i=="]":
                if len(st)!=0 and i==dicts[st[-1]]:
                    st.pop()
                else:
                    return False
        if len(st)==0:
            return True
        else:
            return False
                