from fractions import Fraction


class Tree():
    def __init__(self, op, a, b):
        self.op = op
        self.a = Leaf(a) if isinstance(a, int) else a
        self.b = Leaf(b) if isinstance(b, int) else b

    def __str__(self):
        a = str(self.a)
        b = str(self.b)
        if self.op in ['*', '/']:
            if isinstance(self.a, Tree) and self.a.op in ['+', '-']:
                a = f'({a})'
            if isinstance(self.b, Tree) and self.b.op in ['+', '-']:
                b = f'({b})'
        elif self.op == '-' and isinstance(self.b, Tree) and self.b.op == '-':
            b = f'({b})'
        return a + self.op + b

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
