#!/usr/bin/env python
"""
Connecting Existing Sockets
<https://docs.python.org/3/library/asyncio-protocol.html>

Wait until a socket receives data using the ``loop.create_connection()`` method
with a protocol
"""

import asyncio
from socket import socketpair
from typing import Self

class MyProtocol(asyncio.Protocol):
    def __init__(
            self: Self,
            on_con_lost: asyncio.Future) -> None:
        self.tramsport = None
        self.on_con_lost = on_con_lost

    def connection_made(
            self: Self,
            transport: asyncio.BaseTransport) -> None:
        self.transport = transport

    def data_received(
            self: Self,
            data: bytes) -> None:
        print("Received:", data.decode())

        # We are done: close the transport;
        # connection_lost() will be called automatically.
        self.transport.close()

    def connection_lost(
            self: Self,
            _: Exception | None) -> None:
        # The socket has been closed
        self.on_con_lost.set_result(True)

async def main() -> None:
    # Get a reference to the event loop as we plan to use low-level APIs.
    loop = asyncio.get_running_loop()
    on_con_lost = loop.create_future()

    # Create a pair of connected sockets
    rsock, wsock = socketpair()

    # Register the socket to wait for data
    transport, protocol = await loop.create_connection(
        lambda: MyProtocol(on_con_lost),
        sock=rsock)

    # Simulate the reception of data from the network
    loop.call_soon(wsock.send, 'abc'.encode())

    try:
        await protocol.on_con_lost
    finally:
        transport.close()
        wsock.close()

if __name__ == '__main__':
    asyncio.run(main())
