class User:
    age = 0
    def __init__(self, name):
        print("я создался")
        self.userName = name

    def sayName(self):
        print("Меня зовут ", self.userName)

    def sayAge(self):
        print(self.age)

    def setAge(self, newAge):
        self.age = newAge

    def addCard(self, card):
        self.card = card

    def getCard(self):
        return self.card