from curses.ascii import isdigit


class Calculator:
    def add(self, a, b):
        try:
            return int(a) + int(b)
        except TypeError:
            return "Invalid input"

    def subtract(self, a, b):
        try:
            return int(a) - int(b)
        except TypeError:
            return "Invalid input"

    def multiply(self, a, b):
        if a.isdigit() and b.isdigit():
            return int(a) * int(b)
        else:
            return "Invalid input"

    def divide(self, a, b):
        if a.isdigit() and b.isdigit():
            if b != '0':
                return int(a) / int(b)
            else:
                return "Division by zero"
        else:
            return "Invalid input"