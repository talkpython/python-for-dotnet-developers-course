import datetime

import warnings
import contextlib

import requests
from urllib3.exceptions import InsecureRequestWarning


def main():
    url = input("What's the URL? ").strip()
    times = int(input("How many rounds <num>? "))

    print(f"Running timing against {url}, {times} times.")
    total_time = 0.0
    with no_ssl_verification():
        with requests.Session() as session:
            for _ in range(0, times):
                t0 = datetime.datetime.now()

                resp = session.get(url)
                resp.raise_for_status()
                resp.close()

                dt = datetime.datetime.now() - t0
                total_time += dt.total_seconds()

    print(f"Done in {total_time * 1000:.3f}, that's {total_time / times * 1000:.3f} ms on average.")


old_merge_environment_settings = requests.Session.merge_environment_settings


@contextlib.contextmanager
def no_ssl_verification():
    opened_adapters = set()

    def merge_environment_settings(self, url, proxies, stream, verify, cert):
        # Verification happens only once per connection so we need to close
        # all the opened adapters once we're done. Otherwise, the effects of
        # verify=False persist beyond the end of this context manager.
        opened_adapters.add(self.get_adapter(url))

        settings = old_merge_environment_settings(self, url, proxies, stream, verify, cert)
        settings['verify'] = False

        return settings

    requests.Session.merge_environment_settings = merge_environment_settings

    try:
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', InsecureRequestWarning)
            yield
    finally:
        requests.Session.merge_environment_settings = old_merge_environment_settings

        for adapter in opened_adapters:
            try:
                adapter.close()
            except:
                pass


if __name__ == '__main__':
    main()
