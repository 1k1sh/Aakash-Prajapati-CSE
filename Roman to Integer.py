class Solution:
    def romanToInt(self, s: str) -> int:
        dicts={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        dicts2={"V":"I","X":"I","L":"X","C":"X","D":"C","M":"C"}
        sums=0
        temp=[]
        for i in reversed(range(len(s))):
            if s[i]in ["I","V","X","D","C","M","L"] and sums==0:
                temp.append(s[i])
                sums=dicts[s[i]]+sums
        
            elif dicts[s[i]]>=dicts[temp[-1]]:
                temp.append(s[i])
                sums+=dicts[s[i]]
            elif s[i]==dicts2[temp[-1]]:
                sums-=dicts[s[i]]
        return sums      