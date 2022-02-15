# In a new Python file, create a class of students.
# It should contain the following attributes: name, age, and 
# class with default value "student".
# It should also contain a method which takes in 3 test 
# scores and prints the students average test score.

class Students:

    def __init__(self,age, name="Student"):
        self.name = name
        self.age = age
    def av(self,m1,m2,m3):
        return (m1+m2+m3)/3    

John = Students(21)
Jane = Students(22)
Adam = Students(24)
print(Adam.av(5,6,7))
   
