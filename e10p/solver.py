import itertools
from .node import Tree


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
                t = Tree(op, nums[0], nums[1])
                if t.value():
                    return str(t)
        else:
            for x, y in itertools.permutations(nums):
                z = nums[:]
                z.remove(x)
                z.remove(y)
                for op in ['+', '-', '*', '/']:
                    t = Tree(op, x, y)
                    if t.value():
                        s = self.solv(z + [t])
                        if s:
                            return s
            return None
