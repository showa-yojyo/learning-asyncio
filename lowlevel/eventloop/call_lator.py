#!/usr/bin/env python
"""
Display the current date with call_later()
<https://docs.python.org/3/library/asyncio-eventloop.html#examples>

An example of a callback displaying the current date every second. The callback
uses the ``loop.call_later()`` method to reschedule itself after 5 seconds, and
then stops the event loop:
"""

import asyncio
from datetime import datetime

def display_date(
        end_time: float,
        loop: asyncio.AbstractEventLoop) -> None:
    print(f'{datetime.now():%T.%f}'[:-3], end='\r')

    if loop.time() + 1.0 < end_time:
        loop.call_later(0.1, display_date, end_time, loop)
    else:
        print()
        loop.stop()

def main() -> None:
    loop = asyncio.new_event_loop()

    # Schedule the first call to display_date()
    end_time = loop.time() + 5.0
    loop.call_soon(display_date, end_time, loop)

    # Blocking call interrupted by loop.stop()
    try:
        loop.run_forever()
    finally:
        loop.close()

if __name__ == '__main__':
    main()
