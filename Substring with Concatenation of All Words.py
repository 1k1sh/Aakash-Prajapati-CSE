class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word=[]
        count=0
        ans=[]
        k=len(words[0])
        for i in range(0,len(s)):
            word.clear()
            word=words.copy()
            if len(s)-i>=len(words)*k:
                t=i
                while len(word)!=0:
                    if s[t:t+k] in word:
                        word.remove(s[t:t+k])
                        t+=k
                    else:
                        break
                if len(word)==0:
                    ans.append(i)
        return ans