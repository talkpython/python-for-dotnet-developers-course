from colorama import Fore
import httpx
import bs4


def main():
    print('Using Python packages')

    get_titles()


def get_html(n: int) -> str:
    print(Fore.YELLOW + f'Getting HTML for episode {n}...', flush=True)
    url = f'https://talkpython.fm/{n}'

    resp = httpx.get(url, follow_redirects=True)
    resp.raise_for_status()

    return resp.text


def get_title_from_html(n: int, html: str) -> str:
    print(Fore.CYAN + f'Getting TITLE for episode {n}...', flush=True)

    soup = bs4.BeautifulSoup(html, 'html.parser')
    header = soup.select_one('h1')
    if not header:
        return 'MISSING'

    return header.text.strip()


def get_titles():
    for n in range(220, 230):
        html = get_html(n)
        title = get_title_from_html(n, html)
        print(Fore.GREEN + title)


if __name__ == '__main__':
    main()
