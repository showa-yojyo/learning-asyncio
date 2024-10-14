#!/usr/bin/env python

"""
Event
<https://docs.python.org/3/library/asyncio-sync.html#asyncio-example-sync-event>

An asyncio event can be used to notify multiple asyncio tasks that some event
has happened.

An ``Event`` object manages an internal flag that can be set to true with the
``set()`` method and reset to `false` with the ``clear()`` method. The
``wait()`` method blocks until the flag is set to `true`. The flag is set to
`false` initially.
"""

import asyncio

async def waiter(event: asyncio.Event) -> None:
    print('waiting for it ...')
    await event.wait()
    print('... got it!')

async def main() -> None:
    # Create an Event object.
    event = asyncio.Event()

    # Spawn a Task to wait until 'event' is set.
    waiter_task = asyncio.create_task(waiter(event))

    # Sleep for 1 second and set the event.
    await asyncio.sleep(1)
    event.set()

    # Wait until the waiter task is finished.
    await waiter_task

if __name__ == '__main__':
    asyncio.run(main())
