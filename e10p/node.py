from fractions import Fraction


class Tree():
    def __init__(self, op, a, b):
        self.op = op
        self.a = Leaf(a) if isinstance(a, int) else a
        self.b = Leaf(b) if isinstance(b, int) else b

    def __str__(self):
        s = str(self.a) + self.op + str(self.b)
        if self.op in ['+', '-']:
            return f'({s})'
        else:
            return s

    def value(self):
        if self.op == '+':
            return self.a.value() + self.b.value()
        elif self.op == '-':
            return self.a.value() - self.b.value()
        elif self.op == '*':
            return self.a.value() * self.b.value()
        elif self.op == '/' and not self.b.value() == 0:
            return self.a.value() / self.b.value()
        else:
            return None


class Leaf():
    def __init__(self, v):
        self.v = Fraction(v)

    def __str__(self):
        return str(self.v)

    def value(self):
        return self.v
