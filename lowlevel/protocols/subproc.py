#!/usr/bin/env python
"""
``loop.subprocess_exec()`` and SubprocessProtocol

<https://docs.python.org/3/library/asyncio-protocol.html>

An example of a subprocess protocol used to get the output of a subprocess and
to wait for the subprocess exit.

The subprocess is created by the ``loop.subprocess_exec()`` method:
"""

import asyncio
import sys
from typing import Self

class DateProtocol(asyncio.SubprocessProtocol):
    def __init__(
            self: Self,
            exit_future: asyncio.Future) -> None:
        self.exit_future = exit_future
        self.output = bytearray()
        self.pipe_closed = False
        self.exited = False

    def pipe_connection_lost(
            self: Self,
            fd: int,
            exc: Exception | None) -> None:
        self.pipe_closed = True
        self.check_for_exit()

    def pipe_data_received(
            self: Self,
            fd: int,
            data: bytes) -> None:
        self.output.extend(data)

    def process_exited(self: Self) -> None:
        self.exited = True
        # ``process_exited()`` method can be called before
        # ``pipe_connection_lost()`` method: wait until both methods are called.
        self.check_for_exit()

    def check_for_exit(self: Self) -> None:
        if self.pipe_closed and self.exited:
            self.exit_future.set_result(True)

async def get_date() -> str:
    # Get a reference to the event loop as we plan to use low-level APIs.
    loop = asyncio.get_running_loop()

    code = 'import datetime; print(datetime.datetime.now())'
    exit_future: asyncio.Future = asyncio.Future(loop=loop)

    # Create the subprocess controlled by the protocol DateProtocol,
    # redirect the standard output into a pipe
    transport, protocol = await loop.subprocess_exec(
        lambda: DateProtocol(exit_future),
        sys.executable, '-c', code,
        stdin=None, stderr=None)

    # Wait for the subprocess exit using the process_exited() method of the
    # protocol
    await exit_future

    # Close the stdout pipe
    transport.close()

    # Read the output which was collected by the pipe_data_received() method of
    # the protocol
    data = bytes(protocol.output)
    return data.decode('ascii').rstrip()

if __name__ == '__main__':
    date = asyncio.run(get_date())
    print(f'Current date: {date}')
