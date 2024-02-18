
class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print(f'Hi, I am {self.name}.')


alex = Person("Alex")
alex.talk()

filip = Person("Filip")
filip.talk()



