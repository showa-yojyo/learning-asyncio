#!/usr/bin/env python

"""
Subprocesses <https://docs.python.org/3/library/asyncio-subprocess.html>

An example using the Process class to control a subprocess and the StreamReader
class to read from its standard output.

The subprocess is created by the create_subprocess_exec() function:
"""

import asyncio
import sys

async def get_date() -> str:
    code = 'import datetime; print(datetime.datetime.now())'

    # Create the subprocess; redirect the standard output
    # into a pipe.
    proc = await asyncio.create_subprocess_exec(
        sys.executable, '-c', code,
        stdout=asyncio.subprocess.PIPE)

    # Read one line of output.
    out = proc.stdout
    assert out
    data = await out.readline()
    line = data.decode('ascii').rstrip()

    # Wait for the subprocess exit.
    await proc.wait()
    return line

if __name__ == '__main__':
    date = asyncio.run(get_date())
    print(f"Current date: {date}")
