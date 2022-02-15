class Dice:
    def __init__(self,sides):
        self.side=sides
    def knowside(self):
        return self.side
die1=Dice(6)      
die2=Dice(20)      
die3=Dice(2)      
die4=Dice(4)    
print(die4.knowside())    
