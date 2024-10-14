#!/usr/bin/env python
"""
Task Groups > Terminating a Task Group
<https://docs.python.org/3/library/asyncio-task.html#terminating-a-task-group>
"""

import asyncio
from asyncio import TaskGroup
from typing import Never

class TerminateTaskGroup(Exception):
    """Exception raised to terminate a task group."""

async def force_terminate_task_group() -> Never:
    """Used to force termination of a task group."""
    raise TerminateTaskGroup()

async def job(task_id: int, sleep_time: float) -> None:
    print(f'Task {task_id}: start')
    await asyncio.sleep(sleep_time)
    print(f'Task {task_id}: done')

async def main() -> None:
    try:
        async with TaskGroup() as tg:
            # spawn some tasks
            tg.create_task(job(1, 0.5))
            tg.create_task(job(2, 1.5))
            # sleep for 1 second
            await asyncio.sleep(1)
            # add an exception-raising task to force the group to terminate
            tg.create_task(force_terminate_task_group())
    except* TerminateTaskGroup as ttg:
        print(f"XXXX {ttg}")

if __name__ == '__main__':
    asyncio.run(main())
