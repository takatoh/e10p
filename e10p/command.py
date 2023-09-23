from .solver import Solver
from . import __version__
import argparse


def main():
    args = parse_arguments()
    solver = Solver(4, 10)
    result = solver.solv(args.nums)
    if result:
        print(result)
    else:
        print('No answer found.')


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
        '-V', '--version',
        action='version',
        version=f'v{__version__}',
        help='show version and exit'
    )
    args = parser.parse_args()
    return args
