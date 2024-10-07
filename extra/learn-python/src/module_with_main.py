def sum_of_ints(n: int) -> int:
    """ computes the sum of the first $n$ integers, including the argument """
    return sum(i * i for i in range(1, n + 1))


if __name__ == "__main__":
    from time import time

    for n in range(28):
        start_time = time()
        sum_of_ints(2**n)
        elapsed = time() - start_time
        print(f"f({2**n}) took {elapsed}s")
