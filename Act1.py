#Class is the blueprint
class Student:
    #Properties/Attributes
    #init is inbuilt function
    def __init__(self, name, age, grade, hobby):
        self.name = name
        self.age = age
        self.grade = grade
        self.hobby = hobby
        self.intro = " "

    #Functions/Methods
    def displayDetails(self):
        print("The Details of the Student: ")
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Grade: ",self.grade)
        print("Hobby: ",self.hobby)

    def introduction(self):
        self.intro=input("Tell me about yourself: ")
        print(self.intro)

#Creating Object - instance of a class
#once a class is created, it will call innit function
s1=Student("Remi",12,"6th Grade", "Coding")
#ObjectName.functionName()
s1.displayDetails()
s1.introduction()


s2=Student("James",50,"6th Grade", "Teaching")
s2.displayDetails()
s2.introduction()

