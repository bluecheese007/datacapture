import random
import time

from core.data_capture import DataCapture


def main():
    capture = DataCapture()
    # generate 1000000 random numbers between 0 and 1000
    for _ in range(1000000):
        capture.add(random.randint(0, 1000))

    stats = capture.build_stats()

    start = time.time()
    # print the number of numbers less than 100
    print(stats.less(100))
    # print the number of numbers between 100 and 200
    print(stats.between(100, 200))
    # print the number of numbers greater than 900
    print(stats.greater(900))
    end = time.time()

    print(f"Time taken: {end - start}")


if __name__ == "__main__":
    main()
