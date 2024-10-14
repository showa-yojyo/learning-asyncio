#!/usr/bin/env python
"""
Hello World with call_soon()
<https://docs.python.org/3/library/asyncio-eventloop.html#examples>

An example using the ``loop.call_soon()`` method to schedule a callback. The
callback displays "Hello World" and then stops the event loop:
"""
import asyncio

def hello_world(loop: asyncio.AbstractEventLoop) -> None:
    print('Hello world')
    loop.stop()

def main() -> None:
    loop = asyncio.new_event_loop()

    # Schedule a call to hello_world()
    loop.call_soon(hello_world, loop)

    # Blocking call interrupted by loop.stop()
    try:
        loop.run_forever()
    finally:
        loop.close()

if __name__ == '__main__':
    main()
