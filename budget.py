# Goal: “Create a Budget class that can instantiate objects based on 
# different budget categories like food, clothing, and entertainment.
# These objects should allow for depositing and withdrawing funds 
# from each category, as well computing category balances and 
# transferring balance amounts between categories”


class Budget:
    obj=[]
    def __init__(self, category):
        self.amount=0
        self.category=category
        self.obj.append(self)

    def deposit(self,amount):
        self.amount += amount


    def withdraw(self,amount):
        self.amount -=amount
           
    def balance(self):
        return self.amount
    
    def transfer(self,amount,category):
      self.amount-=amount
      category.amount+=amount

food=Budget("food")
clothing=Budget("clothing")
entertainment=Budget("entertainment")
food.deposit(100)
food.withdraw(12)
food.transfer(50,clothing)
food.transfer(10,entertainment)
print (food.amount,clothing.balance(),entertainment.balance())
t=0
for a in food.obj:
    t+=a.amount
print (t)