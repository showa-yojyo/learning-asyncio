#!/usr/bin/env python

"""
Subprocesses <https://docs.python.org/3/library/asyncio-subprocess.html>

Here's an example of how asyncio can run a shell command and obtain its result
"""

import asyncio

async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')

async def main() -> None:
    await asyncio.gather(
        run('ls /zzz'),
        run('sleep 1; echo "hello"'))

if __name__ == '__main__':
    asyncio.run(main())
