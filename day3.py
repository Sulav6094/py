# def a(b):
#     s=input("ss")
#     return s,b
  
# print(a(3))

#The program should take the students name, homework score (/25),
# assessment score (/50) and final exam score (/100) 
# as inputs, and output their name and final ICT grade as a percentage.
#Function
# def percentage(s,hs,ass,f):
#     return (s,(hs*4+ass*2+f)/3,(hs+ass+f)/1.75)
# s=input("Name ")
# hs=float(input("Homework score/25 "))
# ass=float(input("Assessment score/50 "))
# f=float(input("Finalscore/100 "))
# print(percentage(s,15,35,83)) 
# print(percentage(s,hs,ass,f)) 

#7
# def UL(a):
#     u=0
#     l=0
#     for b in a:
#         if b.islower():
#             l+=1
#         elif b.isupper():
#             u+=1    
#     return(l,u)        
# print ("lower",UL("Hello deS")[0],"upper",UL("Hello deS")[1])  
  
#8
# def li(l):
#     return(list(set(l)))
# print(li([1,2,2,3,3,4]))    

#13
# def p(m):
#     m=m-1
#     l=[1]
#     print(l)
#     for a in range(m):
#         s=[1]
#         for b in range(len(l)):
#             if b==len(l)-1:
#                 s.append(l[0])
#             else:
#                 s.append(l[b]+l[b+1])
#         l=s
#         print(l)        
# p(5)           
# 
#Exercise 1
# price={"Burger":5}
# user_funds = 10.31
# item_price = price["Burger"]

# if item_price < user_funds:
#     print("You have enough money!")
# if item_price == user_funds:
#     print("You have the precise amount of money")
# if item_price < user_funds:
#     print("Sorry you don't have enough money")

# Exercise 2
# def product(n):
#     total = 1
#     for i in n:
#         total *= i
#     return total

#print(product([4,4,5]))

# Exercise 3
# def is_prime(x):
#     if x < 2:
#         return False
#     else:
#         for n in range(2, x-1):
#             if x % n == 0:
#                 return False
#         return True
# for a in [2, 3, 4, 5, 6, 7, 15, 20, 25]:
#     print(f"{a} is prime is {is_prime(a)}")        
# Test the is_prime function with 2, 3, 4, 5, 6, 7, 15, 20 & 25

# Exercise 4
# item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
# n = 0

# while n < 5:
#     n+=1
#     for i in item_list:
#         print(i)
# print (item_list[4])
 
#ascending order
# ra="red-blue-green-yellow"
# items=ra.split('-')
# items=[n for n in input().split('-')]
# items.sort()
# print('-'.join(items))





