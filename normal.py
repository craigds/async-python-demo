"""
Synchronous python demonstration.
© 2021 Craig de Stigter; https://github.com/craigds
BSD 2-clause license.


Prerequisite:
    pip install -r requirements.txt
"""
import requests
import time


def get_url(url):
    print(f"starting to get {url}")
    start_time = time.monotonic()
    response = requests.get(url)
    time_elapsed = time.monotonic() - start_time
    print(f"got {url} in {time_elapsed:.3f}s!")
    print()
    return response


def main():
    start_time = time.monotonic()
    responses = []
    responses.append(get_url("http://example.com"))
    responses.append(get_url("http://example.com/a"))
    responses.append(get_url("http://example.com/b"))
    responses.append(get_url("http://example.com/c"))

    # wait for all the above, then do something else
    get_url("http://example.com/final_url")

    time_elapsed = time.monotonic() - start_time
    print(f"did everything in {time_elapsed:.3f}s")


if __name__ == "__main__":
    main()
