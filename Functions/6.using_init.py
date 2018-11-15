class student:
    def __init__(self,name,dept):
        self.name=name
        self.dept=dept
        
    def display_dat(self):
        print("Name is:",self.name)
        print("dept is:",self.dept)


student('sathish','ece').display_dat()
