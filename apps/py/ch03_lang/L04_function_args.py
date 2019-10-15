def main():
    print("say_hello()")
    say_hello()
    print()

    print("say_hello(name)")
    say_hello("Zoe")
    print()

    print("say_hello(name, times)")
    say_hello("Zoe", 5)
    print()

    print("say_hello(name, times, 1, 2, 3, 4)")
    say_hello("Zoe", 5, 1, 2, 3, 4)
    print()

    print("say_hello(name, times, 1, 2, 3, 4, val=7, mode=prod)")
    say_hello("Zoe", 5, 1, 2, 3, 4, val=7, mode="prod")
    print()

    # THis isn't really an option
    # print("say_hello(int)")
    # say_hello(7)
    # print()

    # print("say_hello(double)")
    # say_hello(5.0)
    # print()


def say_hello(name='friend', times=1, *args, **kwargs):
    print(f"Hello {name} with times={times}, args={args}, kwargs={kwargs}!")


if __name__ == '__main__':
    main()
