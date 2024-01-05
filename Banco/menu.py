class Menu():
    def __init__(self, options):
        self.options = options

    def showOptions(self):
        i = 1
        for option in self.options:
            print(f'{i}\t{option}')
            i += 1