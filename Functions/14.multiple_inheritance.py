class programmer:
    def show(self):
        print('I am Programmer')

class network_eng:
    def disp(self):
        print('I am Network Engineer')

class hacker(programmer,network_eng):
    def printing(self):
        print('I am Hacker')

a=hacker()
a.printing()
a.disp()
a.show()
