from fractions import Fraction


class Node():
    def __init__(self, op, a, b):
        self.op = op
        self.a = Fraction(a)
        self.b = Fraction(b)

    def __str__(self):
        s = str(self.a) + self.op + str(self.b)
        if self.op in ['+', '-']:
            return f'{{s}}'
        else:
            return s

    def value(self):
        if self.op == '+':
            return self.a + self.b
        elif self.op == '-':
            return self.a - self.b
        elif self.op == '*':
            return self.a * self.b
        elif self.op == '/' and not self.b == 0:
            return self.a / self.b
        else:
            return None
