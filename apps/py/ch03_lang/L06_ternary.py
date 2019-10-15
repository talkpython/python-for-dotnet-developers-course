def main():
    while True:
        text = input("Enter a number: ")
        if not text:
            print("Later...")
            break

        num = int(text)
        num_class = "small" if num < 100 else "huge!"
        print(f"The number is {num_class}")
