from switchlang import switch, closed_range


def main():
    while True:

        text = input("Enter a number between 1 & 4: ")
        if not text:
            print("Later!")
            break

        num = int(text)

        with switch(num) as s:
            s.case(1, lambda: print("One is fun!"))
            s.case(2, lambda: print("2 * 2 = 4"))
            s.case(3, lambda: print("Three and free."))
            s.case(4, lambda: print("4 more!"))
            s.case(closed_range(10, 20), lambda: num * num)
            s.default(lambda: print(f"Say what? {num}."))

        print(f"Done and got {s.result}")


if __name__ == '__main__':
    main()
