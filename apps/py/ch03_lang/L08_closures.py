def main():
    counter1 = create_counter(7, 1)
    counter2 = create_counter(-100, 2)

    counter1()
    counter2()
    counter1()
    counter2()
    counter1()
    counter2()


def create_counter(start_val, counter_id):
    print(f"Creating a counter with start value {start_val}...")

    inc = start_val

    def counter():
        nonlocal inc
        inc += 1
        print(f"#{counter_id}: Counting {start_val}\t -->\t{inc}.")

    return counter


if __name__ == '__main__':
    main()
