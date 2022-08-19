class doublyll:
    def __init__(self, data, next=None, pre=None):
        self.data=data
        self.pre=pre
        self.next=next
    def __str__(self):
        return(f"{self.data},{self.next}")
    
d1=doublyll(2,doublyll(3,(doublyll(4,doublyll(5)))))
print(d1)
