#!/usr/bin/env python

"""
Detect never-retrieved exceptions
<https://docs.python.org/3/library/asyncio-dev.html>

If a ``Future.set_exception()`` is called but the ``Future`` object is never
awaited on, the exception would never be propagated to the user code. In this
case, ``asyncio`` would emit a log message when the ``Future`` object is garbage
collected.
"""

import asyncio

async def bug() -> None:
    raise Exception("not consumed")

async def main() -> None:
    asyncio.create_task(bug())

if __name__ == '__main__':
    # Enable the debug mode to get the traceback where the task was created:
    asyncio.run(main(), debug=True)
