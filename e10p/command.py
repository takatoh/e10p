import argparse
from .solver import Solver


def main():
    args = parse_arguments()
    solver = Solver(4, 10)
    result = solver.solv(args.nums)
    print(result)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'nums',
        action='store',
        nargs='+',
        type=int,
        help='specify numbers'
    )
    args = parser.parse_args()
    return args
