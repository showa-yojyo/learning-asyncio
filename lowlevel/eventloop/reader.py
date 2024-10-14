#!/usr/bin/env python
"""
Watch a file descriptor for read events
<https://docs.python.org/3/library/asyncio-eventloop.html#examples>

Wait until a file descriptor received some data using the ``loop.add_reader()``
method and then close the event loop
"""

import asyncio
from socket import socketpair

def main() -> None:
    # Create a pair of connected file descriptors
    rsock, wsock = socketpair()

    loop = asyncio.new_event_loop()

    def reader() -> None:
        data = rsock.recv(100)
        print("Received:", data.decode())
        # We are done: unregister the file descriptor
        loop.remove_reader(rsock)
        # Stop the event loop
        loop.stop()

    # Register the file descriptor for read event
    loop.add_reader(rsock, reader)

    # Simulate the reception of data from the network
    loop.call_soon(wsock.send, 'abc'.encode())

    try:
        # Run the event loop
        loop.run_forever()
    finally:
        # We are done, close sockets and the event loop
        rsock.close()
        wsock.close()
        loop.close()

if __name__ == '__main__':
    main()
