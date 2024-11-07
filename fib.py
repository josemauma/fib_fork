import argparse

cache = {}


def fibonacci_recursive(n: int) -> int:
    """
    Computes the n-th Fibonacci number.
    :param n: n-th Fibonacci number.
    :return: The n-th Fibonacci number.
    """
    # TODO: Implement!

    if n < 0:
        raise ValueError("n must be greater than or equal to 0.")
    if n < 2:
        return n

    if n in cache:
        return cache[n]

    nth = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

    cache[n] = nth


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('nth', type=int, help="Nth Fibonacci number.")

    args = parser.parse_args()
    nth = fibonacci_iterative(args.nth)
    print(nth)

    # n = int(args[1])
    # nth = fibonacci_iterative(n)
    # print(nth)
