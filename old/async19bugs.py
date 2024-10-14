#!/usr/bin/env python
"""async19.py: Chain coroutines (with bugs)

Usage:
  async19.py
"""

import asyncio

async def create() -> None:
    await asyncio.sleep(3.0)
    print("(1) create file")

async def write() -> None:
    await asyncio.sleep(1.0)
    print("(2) write into file")

async def close() -> None:
    print("(3) close file")

async def test(loop: asyncio.AbstractEventLoop) -> None:
    asyncio.ensure_future(create())
    asyncio.ensure_future(write())
    asyncio.ensure_future(close())
    await asyncio.sleep(2.0)
    loop.stop()

def main() -> None:
    loop = asyncio.new_event_loop()
    asyncio.ensure_future(test(loop), loop=loop)
    loop.run_forever()
    print(f"Pending tasks at exit: {asyncio.all_tasks(loop)}")
    loop.close()

if __name__ == '__main__':
    main()
