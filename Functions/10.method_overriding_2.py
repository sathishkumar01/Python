class a:
    def display(self):
        print("hai welcome to Class A")

class b(a):
    def display(self):
        print("hai welcome to Class B")


a1=b()
a1.display()
a2=a()
a2.display()
