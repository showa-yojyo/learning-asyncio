#!/usr/bin/env python
"""async08future.py: Use Future and ensure_future
cf. async09callback.py

Usage:
  async08future.py
"""
import asyncio

async def slow_operation(future: asyncio.Future) -> None:
    await asyncio.sleep(1)
    future.set_result('Future is done!')

def main() -> None:
    loop = asyncio.new_event_loop()
    future = loop.create_future()
    try:
        loop.run_until_complete(slow_operation(future))
        print(future.result())
    finally:
        loop.close()

if __name__ == '__main__':
    main()
