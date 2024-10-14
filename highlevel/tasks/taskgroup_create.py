#!/usr/bin/env python
"""
Task Groups
<https://docs.python.org/3/library/asyncio-task.html#asyncio.TaskGroup>
"""

import asyncio

async def some_coro() -> int:
    return 42

async def another_coro() -> int:
    return 2459

async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(some_coro())
        task2 = tg.create_task(another_coro())
    print(f"Both tasks have completed now: {task1.result()}, {task2.result()}")

if __name__ == '__main__':
    asyncio.run(main())
