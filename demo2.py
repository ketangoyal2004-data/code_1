class std:
    def name(self,name):
        self.name = name
        print("My name is :",name)

    def course(self,course):
        self.course = course
        print("My course is :",course)

obj = std()
obj.name("John")
obj.course("Python")    