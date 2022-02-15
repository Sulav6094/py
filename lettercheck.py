class Lettercheck:
    def __init__(self,var):
        self.v=var
    def vowl(self,var):
        if var.upper() in self.v:
            return True
        else:
            return False
a=Lettercheck("ABCDE")
print(a.vowl("p"))                
b=Lettercheck("AEIOU")
print(b.vowl("p"))