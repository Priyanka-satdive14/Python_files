class Bird:
    def __init__(self) :
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaah...')
            self.hungry = False
        else:
            print('I am full, no thanks!')

b= Bird()
b.eat() #1st time feed output will be true
b.eat()

class SongBird(Bird):
    def __init__(self):
        super(SongBird,self).__init__()
        self.sound = 'Squawk!'
    def sing(self):
        print(f'Singing{self.sound} {self.sound}!')
    def eat(self):
        if self.hungry:
            print('Pheu...')
            self.hungry = False
        else:
            print('No thanks,Had enough')
    

sb = SongBird()
sb.sing()
sb.eat()
sb.eat()