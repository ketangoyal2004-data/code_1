class cal:
    @staticmethod
    def add(a,b):
        return a + b
    
    @staticmethod
    def sub(a,b):
        return a - b 
    
    @staticmethod
    def mul(a,b):
        return a * b
    
    @staticmethod
    def div(a,b):
        return a / b
    

obj = cal()
print(obj.add(10,20))
print(obj.sub(10,20))
print(obj.mul(10,20))
print(obj.div(10,20))   