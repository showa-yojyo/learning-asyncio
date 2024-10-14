#!/usr/bin/env python
"""
Running Tasks Concurrently
<https://docs.python.org/3/library/asyncio-task.html#asyncio.gather>
"""
import asyncio

async def factorial(name: str, number: int) -> int:
    """Return $n!$
    """

    # コメント：最適化がなされていないのは意図的だ

    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({i}) = {f}")
    return f

async def main() -> None:
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)

if __name__ == '__main__':
    asyncio.run(main())
