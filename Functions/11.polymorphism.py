class dog:
    def sound(self):
        print("bow bow")

class cat:
    def sound(self):
        print("Meow Meow")

def makesound(animaltype):
    animaltype.sound()

a1=dog()
a2=cat()

makesound(a1)
makesound(a2)
