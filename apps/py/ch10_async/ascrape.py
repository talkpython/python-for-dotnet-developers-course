from colorama import Fore
import httpx
import bs4
import datetime


def main():
    print("Python async web scraper")

    t0 = datetime.datetime.now()
    get_titles()
    dt = datetime.datetime.now() - t0
    print(f"Finished in {dt.total_seconds():,.2f} seconds.")


def get_html(n: int) -> str:
    print(Fore.YELLOW + f"Getting HTML for episode {n}...", flush=True)
    url = f'https://talkpython.fm/{n}'

    resp = httpx.get(url)
    resp.raise_for_status()

    return resp.text


def get_title_from_html(n: int, html: str) -> str:
    print(Fore.CYAN + f"Getting TITLE for episode {n}...", flush=True)

    soup = bs4.BeautifulSoup(html, 'html.parser')
    header = soup.select_one('h1')
    if not header:
        return "MISSING"

    return header.text.strip()


def get_titles():
    for n in range(220, 231):
        html = get_html(n)
        title = get_title_from_html(n, html)
        print(Fore.GREEN + title)


if __name__ == '__main__':
    main()
