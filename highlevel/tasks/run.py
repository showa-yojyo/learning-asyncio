#!/usr/bin/env python
"""
Features:
- asyncio.sleep()
- asyncio.run()
"""

import asyncio

async def main() -> None:
    print('Hello ...')
    # コメント：sleep() は与えられた時間後に完了する
    # awaitable object であると考えるのが良い。
    #
    # Awaitable とは coroutines, Task, Future の総称と考えて良い。
    await asyncio.sleep(1)
    print('... World!')

if __name__ == '__main__':
    # コメント：run() の呼び出しで良くなったようだ。
    asyncio.run(main())
