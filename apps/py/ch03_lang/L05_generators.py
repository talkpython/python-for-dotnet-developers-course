def main():
    for n in fibonacci():
        if n > 1000:
            break

        print(n, end=', ')


def fibonacci():
    current, nxt = 0, 1

    while True:
        current, nxt = nxt, nxt + current
        yield current


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
