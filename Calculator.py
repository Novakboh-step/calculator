class Calculator:
    def add(self, a, b):
        mes = f"{a} + {b} = {a + b}"
        print(mes)
        return a + b

    def subtract(self, a, b):
        mes = f"{a} - {b} = {a - b}"
        print(mes)
        return a - b

    def multiply(self, a, b):
        mes = f"{a} * {b} = {a * b}"
        print(mes)
        return a * b

    def divide(self, a, b):
        if b:
            mes = f"{a} / {b} = {a / b}"
            print(mes)
            return a / b
        print("You can`t divide by zero")