import random


def main():
    show_header()

    # Random rand =new Random();
    # the_number = rand.Next(1, 100);
    the_number = random.randint(1, 100)

    count = 0
    while True:
        guess = get_guess()
        if not guess:
            continue

        count += 1
        if evaluate_guess(guess, the_number):
            break

    print(f"You got the number in {count} attempts. Thanks for playing, bye!")


def evaluate_guess(guess, number):
    if guess == number:
        print(f"That's it! I was thinking of {number}.")
    if guess < number:
        print("That's too LOW")
    elif guess > number:
        print("That's too HIGH")

    return guess == number


def get_guess():
    val = None
    try:
        text = input("What number am I thinking of? ")
        val = int(text)
        if val < 1 or 100 < val:
            print(f"{val} is not between 1 and 100.")
            return None
        return val
    except:
        print(f"{val} is not an integer!")
        return None


def show_header():
    print('-------------------------------------------')
    print('|                                         |')
    print('|         PYTHON HIGH / LOW GAME          |')
    print('|                                         |')
    print('-------------------------------------------')
    print()
    print("I'm thinking of a number between 1 & 100. ")
    print("How many steps can you guess it in?")
    print()

    # implicit
    return None


if __name__ == '__main__':
    main()
