class employee:
    
    def get_data(self,name,age):
        self.name=name
        self.age=age
        
    def disp_data(self):
        print("Name of the employee is:",self.name)
        print("Age of the employee is:",self.age)

e=employee()
e.get_data("surya",32)
e.disp_data()
