import json


def main():
    data = {
        "name": "Michael",
        "language": "Python",
    }

    with open('file.json', 'w', encoding='utf-8') as fout:
        json.dump(data, fout, indent=True)

    print("Saved to local file: file.json")


if __name__ == '__main__':
    main()
