class Animal:
    def __init__(self):
        self.num_eyes = 2
        
    def breathe(self):
        print('Inhale, exhale' )
        
class Fish(Animal):
    def __init__(self):
        super().__init__()
        
    def breathe(self):
        super().breathe()
        print('doing it under water')
    
    def swim(self):
        print('moving under water')
        
nemo = Fish()
nemo.breathe()
print(nemo.num_eyes)