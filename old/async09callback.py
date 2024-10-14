#!/usr/bin/env python
"""async09callback.py: Explicitly set callback
cf. async08future.py

Usage:
  async09callback.py
"""

import asyncio

async def slow_operation(future: asyncio.Future) -> None:
    await asyncio.sleep(1)
    future.set_result('Future is done!')

def main() -> None:
    loop = asyncio.new_event_loop()
    future = loop.create_future()
    asyncio.ensure_future(slow_operation(future), loop=loop)

    def got_result(future: asyncio.Future) -> None:
        print(future.result())
        loop.stop()

    future.add_done_callback(got_result)
    try:
        loop.run_forever()
    finally:
        loop.close()

if __name__ == '__main__':
    main()
