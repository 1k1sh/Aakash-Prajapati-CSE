
stac=[2,3,4,5,7,8,9,1,7]

n=9
def push(k):
    
    if len(stac)>=n:
        print("stackpoverflow")
        return
    else:
        stac.append(k)
    
def pop():
    if len(stac)<0:
        print("stackunderflow")
    stac.pop()
   
pop()
print(stac)