class StringHandler:
    def getString(self):
        self.string = input()

    def printString(self):
        print(self.string.upper())


obj = StringHandler()
obj.getString()
obj.printString()