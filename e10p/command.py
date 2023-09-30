from .solver import Solver, InvalidCountOfNumbers
from . import __version__
import argparse


def main():
    args = parse_arguments()
    solver = Solver(args.count, args.expected)
    try:
        result = solver.solv(args.nums)
        if result:
            print(result)
        else:
            print('No answer found.')
    except InvalidCountOfNumbers as e:
        print(e)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Solver for Extended TenPuzzle.'
    )
    parser.add_argument(
        'nums',
        action='store',
        nargs='+',
        type=int,
        metavar='NUM',
        help='specify numbers'
    )
    parser.add_argument(
        '-c', '--count',
        action='store',
        type=int,
        default=4,
        help='specify count of numbers (default to 4)'
    )
    parser.add_argument(
        '-e', '--expected',
        action='store',
        type=int,
        default=10,
        help='specify expected number (default to 10)'
    )
    parser.add_argument(
        '-V', '--version',
        action='version',
        version=f'v{__version__}',
        help='show version and exit'
    )
    args = parser.parse_args()
    return args
