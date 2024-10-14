#!/usr/bin/env python
"""async21syntax.py: Use new syntax ``await with``

Usage:
  async21syntax.py
"""

import asyncio

async def coro(name: int, lock: asyncio.Lock) -> None:
    print(f'coro {name}: waiting for lock')
    async with lock:
        print(f'coro {name}: holding the lock')
        await asyncio.sleep(1)
        print(f'coro {name}: releasing the lock')

async def main() -> None:
    lock = asyncio.Lock()
    await asyncio.gather(
        coro(1, lock),
        coro(2, lock))

if __name__ == '__main__': asyncio.run(main())
