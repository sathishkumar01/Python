class employee:
    def get_data(self,name,age):
        self.name=name
        self.age=age
        
    def disp_data(self):
        print("Name of the employee is:",self.name)
        print("Age of the employee is:",self.age)

e=employee()

name=input('enter name : ')
age=input('enter age : ')

e.get_data(name,age)
e.disp_data()
