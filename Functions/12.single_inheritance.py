class animal:
    def eating(self):
        print('eating')

class dog(animal):
    def sounds(self):
        print('bow bow')

d=dog()
d.sounds()
d.eating()
