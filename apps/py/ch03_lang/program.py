def main():
    name = input("What is your name? ")
    some_method(name)


def some_method(name):
    if name.strip().lower() == 'michael':
        print("Hello old friend!")
    else:
        print(f"Nice to meet you {name}.")
        print("My name is Python!")


if __name__ == '__main__':
    main()
