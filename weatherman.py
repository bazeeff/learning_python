# from report import get_description
#
# description = get_description()
# print("Today's weather:", description)
#
# from report import get_description as do_it
#
# description = do_it()
# print("Today's weather:", description)
class Human:
    def __init__(self, name):
        self.name = name

    def printName(self):
        print(self.name + "human")


class Person(Human):
    def __init__(self, name, doc):
        super().__init__(name)
        self.name = name
        self.doc = doc

    def printName(self):
        print(self.name)

    def printDoc(self):
        print(self.doc)


human = Human('2tema')
person = Person("tema", 'passport')
person.printName()
person.printDoc()
human.printName()

