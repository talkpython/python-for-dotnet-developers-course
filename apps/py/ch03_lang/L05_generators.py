def main():
    pass


def fibonacci_num(count):
    current = 0
    nxt = 1
    nums = []

    for _ in range(0, count):
        current, nxt = nxt, nxt + current
        nums.append(current)

    return nums


if __name__ == '__main__':
    main()
