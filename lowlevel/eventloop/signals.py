#!/usr/bin/env python
"""
Set signal handlers for SIGINT and SIGTERM
<https://docs.python.org/3/library/asyncio-eventloop.html#examples>

Register handlers for signals ``SIGINT`` and ``SIGTERM`` using the
``loop.add_signal_handler()`` method
"""

import asyncio
import functools
import os
import signal

def ask_exit(signame: str, loop: asyncio.AbstractEventLoop) -> None:
    print(f"got signal {signame}: exit")
    loop.stop()

async def main() -> None:
    loop = asyncio.get_running_loop()
    for signame in {'SIGINT', 'SIGTERM'}:
        loop.add_signal_handler(
            getattr(signal, signame),
            functools.partial(ask_exit, signame, loop))

    await asyncio.sleep(60)

if __name__ == '__main__':
    print("Event loop running for 1 hour, press Ctrl+C to interrupt.")
    print(f"pid {os.getpid()}: send SIGINT or SIGTERM to exit.")
    asyncio.run(main())
