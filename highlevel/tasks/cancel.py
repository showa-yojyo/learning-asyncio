#!/usr/bin/env python

"""
Cancellation
<https://docs.python.org/3/library/asyncio-task.html#asyncio-example-task-cancel>

Handling CancelledError to run code on cancellation request.
"""

import asyncio

async def cancel_me() -> None:
    print('cancel_me(): before sleep')

    try:
        # Wait for 1 hour
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')

async def main() -> None:
    # Create a "cancel_me" Task
    task = asyncio.create_task(cancel_me())

    # Wait for 1 second
    await asyncio.sleep(1)

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")

asyncio.run(main())
