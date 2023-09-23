import itertools
from fractions import Fraction
from .node import Node


class Solver():
    def __init__(self, n, expected):
        self.n = n
        self.expected = expected

    def solv(self, nums):
        if len(nums) == 1:
            if nums[0].value() == self.expected:
                return self.expected
            else:
                return None
        elif len(nums) == 2:
            for op in ['+', '-', '*', '/']:
                node = Node(op, nums[0], nums[1])
                if node.value():
                    return str(node)
        else:
            fnums = [ Fraction(n) for n in nums ]
            for x, y in itertools.permutations(fnums):
                z = fnums[:]
                z.remove(x)
                z.remove(y)
                for op in ['+', '-', '*', '/']:
                    node = Node(op, x, y)
                    if node.value():
                        s = self.solv(z + [node])
                        if s:
                            return s
            return None
