from colorama import Fore
import httpx


def main():
    print("Using Python packages")

    get_titles()


def get_html(n: int) -> str:
    print(Fore.YELLOW + f"Getting HTML for episode {n}...")
    url = f'https://talkpython.fm/{n}'

    resp = httpx.get(url)
    resp.raise_for_status()

    return resp.text


def get_titles():
    for n in range(220, 230):
        html = get_html(n)
        title = get_title_from_html(html)


if __name__ == '__main__':
    main()
