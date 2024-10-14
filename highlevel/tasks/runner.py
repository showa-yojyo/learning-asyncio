#!/usr/bin/env python
"""Runner context manager
<https://docs.python.org/3/library/asyncio-runner.html>
"""

import asyncio

async def main() -> None:
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

if __name__ == '__main__':
    with asyncio.Runner() as runner:
        runner.run(main())
