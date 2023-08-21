class Bank:

    def __init__(self,x):
        self.name = "bank1"
    
    def __str__(self):
        return f"{self.name}"
   
    @classmethod
    def setNational(cls, nat):
        cls.national = nat
    
b = Bank()
b.setNational("polish")
print(b.national)