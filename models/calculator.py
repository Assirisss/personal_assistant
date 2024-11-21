from curses.ascii import isdigit


class Calculator:
    def add(self, a, b):
        try:
            return a + b
        except TypeError:
            return "Invalid input"

    def subtract(self, a, b):
        try:
            return a - b
        except TypeError:
            return "Invalid input"

    def multiply(self, a, b):
        if isdigit(a) and isdigit(b):
            return a * b
        else:
            return "Invalid input"

    def divide(self, a, b):
        if isdigit(a) and isdigit(b):
            if b != 0:
                return a / b
            else:
                return "Division by zero"
        else:
            return "Invalid input"