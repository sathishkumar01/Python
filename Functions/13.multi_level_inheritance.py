class person:
    def display(self):
        print('I am Person')

class employee(person):
    def printing(self):
        print('I am Employee')

class programmer(employee):
    def show(self):
        print('I am Programmer')

d=programmer()
d.show()
d.printing()
d.display()
