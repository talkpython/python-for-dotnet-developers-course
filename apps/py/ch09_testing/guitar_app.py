import lib


def main():
    print("Welcome to the guitar app.")
    while True:
        print()
        style = input("What style of guitar do you want to see? ")
        if not style:
            print("cya")
            break

        guitars = lib.all_guitars(style)
        print(f"We found {len(guitars)} guitars.")
        for idx, g in enumerate(guitars, start=1):
            print(f'{idx}. {g.name} for ${g.price:,.0f} ({g.style})')


if __name__ == '__main__':
    main()
