#!/usr/bin/env python
"""async07chain.py: Chain coroutines

Usage:
  async07chain.py
"""
import asyncio

async def compute(x: int, y: int) -> int:
    print(f"Compute {x} + {y} ...")
    await asyncio.sleep(1.0)
    return x + y

async def print_sum(x: int, y: int) -> None:
    result = await compute(x, y)
    print(f"{x} + {y} = {result}")

def main() -> None:
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(print_sum(1, 2))
    finally:
        loop.close()

if __name__ == '__main__':
    main()
