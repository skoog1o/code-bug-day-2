class Greeter:
    def __init__(self, name):
        self.name = name  # fixed name

    def greet(self):      # added self parameter
        print("Hello, " + self.name)

user = Greeter("Matt")
user.greet()
