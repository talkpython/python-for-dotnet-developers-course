from colorama import Fore
import httpx
import bs4
import datetime
import asyncio

loop = asyncio.get_event_loop()


def main():
    print("Python async web scraper")

    t0 = datetime.datetime.now()
    loop.run_until_complete(get_titles())
    dt = datetime.datetime.now() - t0
    print(f"Finished in {dt.total_seconds():,.2f} seconds.")

    loop.close()


async def get_html(n: int) -> str:
    print(Fore.YELLOW + f"Getting HTML for episode {n}...", flush=True)
    url = f'https://talkpython.fm/{n}'

    # The "async with" syntax ensures that all active connections are closed on exit.
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()

    return resp.text


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


async def get_titles():
    tasks = []
    for n in range(220, 231):
        task = loop.create_task(get_html(n))
        episode = n

        tasks.append((episode, task))

    for episode, task in tasks:
        html = await task
        title = get_title_from_html(episode, html)
        print(Fore.GREEN + title)


if __name__ == '__main__':
    main()
