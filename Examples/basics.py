class newProgram():
    def __init__(self, debugging=False):
        self.debugging = debugging
        self.running = True
    def print(self, message):
        print(message)
    def debug(self, message):
        if self.debugging:
            print('[DEBUG] ' + message)

class newUser():
    def __init__(self):
        pass
    def input(self, question):
        return input(question)
