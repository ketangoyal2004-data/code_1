class std:
    def name(self,name):
        self.name = name
        print("My name is :",name)

    def course(self,course):
        self.course = course
        print("My course is :",course)

    def branch(self,branch):
        self.branch = branch
        print("My branch is :",branch)

    def age(self,age):
        self.age = age
        print("My age is :",age)

obj = std()
obj.name("John")
obj.course("Python")    
obj.branch("Computer Science")
obj.age(20)