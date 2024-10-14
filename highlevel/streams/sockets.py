#!/usr/bin/env python
"""
Register an open socket to wait for data using streams
<https://docs.python.org/3/library/asyncio-stream.html>

Coroutine waiting until a socket receives data using the open_connection()
function:
"""

import asyncio
from socket import socketpair

async def wait_for_data() -> None:
    # Get a reference to the current event loop because
    # we want to access low-level APIs.
    loop = asyncio.get_running_loop()

    # Create a pair of connected sockets
    rsock, wsock = socketpair()

    # Register the open socket to wait for data
    reader, writer = await asyncio.open_connection(sock=rsock)

    # Simulate the reception of data from the network
    loop.call_soon(wsock.send, 'abc'.encode())

    # Wait for data
    data = await reader.read(100)

    # Got data, we are done: close the socket
    print("Received:", data.decode())
    writer.close()
    await writer.wait_closed()

    # Close the second socket
    wsock.close()

if __name__ == '__main__':
    asyncio.run(wait_for_data())
