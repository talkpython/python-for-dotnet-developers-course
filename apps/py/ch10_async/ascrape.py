from colorama import Fore
import httpx
import bs4
import datetime
from unsync import unsync


def main():
    print("Python async web scraper")

    t0 = datetime.datetime.now()
    get_titles().result()
    dt = datetime.datetime.now() - t0
    print(f"Finished in {dt.total_seconds():,.2f} seconds.")


@unsync
async def get_html(n: int) -> str:
    print(Fore.YELLOW + f"Getting HTML for episode {n}...", flush=True)
    url = f'https://talkpython.fm/{n}'

    # The "async with" syntax ensures that all active connections are closed on exit.
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()

    return resp.text


# @unsync                # <-- will run get_title_from_html() on a background thread.
# @unsync(cpu_bound=True)  # <-- will run get_title_from_html() on a subprocess.
def get_title_from_html(n: int, html: str) -> str:
    print(Fore.CYAN + f"Getting TITLE for episode {n}...", flush=True)

    soup = bs4.BeautifulSoup(html, 'html.parser')
    header = soup.select_one('h1')
    if not header:
        return "MISSING"

    return header.text.strip()


# async def get_titles():
#     for n in range(220, 231):
#         html = await get_html(n)
#         title = get_title_from_html(n, html)
#         print(Fore.GREEN + title)

@unsync
async def get_titles():
    tasks = []
    for n in range(220, 231):
        task = get_html(n)
        episode = n

        tasks.append((episode, task))

    for episode, task in tasks:
        html = await task
        title = get_title_from_html(episode, html)
        print(Fore.GREEN + title)


if __name__ == '__main__':
    main()
