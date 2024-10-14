#!/usr/bin/env python

"""Timeouts
<https://docs.python.org/3/library/asyncio-task.html#asyncio.wait_for>

Features:
- asyncio.sleep()
- asyncio.wait_for()
- asyncio.run()

Class:
- asyncio.TimeoutError
"""

import asyncio

async def eternity() -> None:
    # Sleep for one hour
    await asyncio.sleep(3600)
    print('yay!')

async def main() -> None:
    # Wait for at most 1 second
    try:
        # Wait for eternity() to complete with a timeout
        # cf. asyncio.wait()
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout!')

asyncio.run(main())
