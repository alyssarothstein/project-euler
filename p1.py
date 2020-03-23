# Problem 1
import argparse


def sum_3_5_divisible(n):
    """Sums integers < n divisible by 3 or 5"""
    sum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, help='An integer limit. Sum ints divisible by 3 or 5 <= n')

    args = parser.parse_args()
    print(sum_3_5_divisible(args.n))
