"""
Asynchronous python demonstration.
© 2021 Craig de Stigter; https://github.com/craigds
BSD 2-clause license.


Prerequisite:
    pip install -r requirements.txt
"""
import time
import asyncio

from aiohttp_requests import requests


async def get_url(url):
    print(f"starting to get {url}")
    start_time = time.monotonic()
    response = await requests.get(url)
    time_elapsed = time.monotonic() - start_time
    print(f"got {url} in {time_elapsed:.3f}s!")
    print()
    return response


async def main():
    start_time = time.monotonic()
    awaitables = []
    awaitables.append(get_url("http://example.com"))
    awaitables.append(get_url("http://example.com/a"))
    awaitables.append(get_url("http://example.com/b"))
    awaitables.append(get_url("http://example.com/c"))

    # wait for all the above, then do something else
    responses = await asyncio.gather(*awaitables)
    await get_url("http://example.com/final_url")

    time_elapsed = time.monotonic() - start_time
    print(f"did everything in {time_elapsed:.3f}s")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
