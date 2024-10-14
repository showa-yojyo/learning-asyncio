#!/usr/bin/env python

"""

<https://docs.python.org/3/library/asyncio-task.html#asyncio-example-task-cancel>
"""

import asyncio

async def make_request() -> None:
    print("make_request")
    await asyncio.sleep(1)

async def make_another_request() -> None:
    print("make_another_request")
    await asyncio.sleep(1)

async def unrelated_code() -> None:
    print("unrelated_code")

async def make_request_with_timeout() -> None:
    try:
        async with asyncio.timeout(1):
            # Structured block affected by the timeout:
            await make_request()
            await make_another_request()
    except TimeoutError:
        print("There was a timeout")
    # Outer code not affected by the timeout:
    await unrelated_code()

if __name__ == '__main__':
    asyncio.run(make_request_with_timeout())
