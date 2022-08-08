def countVowelPermutation(n):
        lis=["a","e","i","o","u"]
        if n==1:
            return 5
            
        while n:
            m=len(lis)
            for i in range(m):
                if lis[i][-1]=="a":
                    #lis[i][-1]=lis[i][-1]+"e"
                    lis.append(lis[i][-1]+"e")
                    lis.remove(lis[i])
                    continue
                    
                if lis[i][-1]=="e":
                    lis.append(lis[i][-1]+"a")
                    lis.append(lis[i][-1]+"i")
                    lis.remove(lis[i])
                    continue
                if lis[i][-1]=="i":
                    lis.append(lis[i][-1]+"a")
                    lis.append(lis[i][-1]+"e")
                    lis.append(lis[i][-1]+"i")
                    lis.append(lis[i][-1]+"o")
                    lis.append(lis[i][-1]+"u")
                    lis.remove(lis[i])
                    continue
                if lis[i][-1]=="o":
                    lis.append(lis[i][-1]+"i")
                    lis.append(lis[i][-1]+"u")
                    lis.remove(lis[i])
                    
                if lis[i][-1]=="u":
                    lis.append(lis[i][-1]+"a")
                    lis.remove(lis[i])
            
                
            n-=1
        liss=list(set(lis)) 
        print(liss)            
        return len(liss)
countVowelPermutation(1)
