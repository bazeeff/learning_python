class Duck:
    def __init__(self, input_name):
        self.__name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.__name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name


fowl = Duck('Donald Duck')
#fowl.name = "Duck Duck"
print(fowl._Duck__name)
#print(fowl.name)
