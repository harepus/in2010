import sort_runner
import sys


def main():
    A = [int(x.strip()) for x in sys.stdin.readlines()]
    filename = "inputs"
    sort_runner.run_algs_part1(A, filename)
    sort_runner.run_algs_part2(A, filename)


if __name__ == '__main__':
    main()
