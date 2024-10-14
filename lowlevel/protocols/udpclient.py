#!/usr/bin/env python
"""
UDP Echo Client <https://docs.python.org/3/library/asyncio-protocol.html>

A UDP echo client, using the ``loop.create_datagram_endpoint()`` method, sends
data and closes the transport when it receives the answer:
"""

import asyncio
from typing import Self

class EchoClientProtocol(asyncio.DatagramProtocol):
    def __init__(
            self: Self,
            message: str,
            on_con_lost: asyncio.Future) -> None:
        super().__init__()
        self.message = message
        self.on_con_lost = on_con_lost
        self.transport: asyncio.BaseTransport

    def connection_made(
            self: Self,
            transport: asyncio.BaseTransport) -> None:
        assert(isinstance(transport, asyncio.DatagramTransport))
        self.transport = transport
        print('Send:', self.message)
        self.transport.sendto(self.message.encode())

    def datagram_received(
            self: Self,
            data: bytes,
            _) -> None:
        print("Received:", data.decode())

        print("Close the socket")
        self.transport.close()

    def error_received(
            self: Self,
            exc: Exception) -> None:
        print('Error received:', exc)

    def connection_lost(
            self: Self,
            _: Exception | None):
        print("Connection closed")
        self.on_con_lost.set_result(True)

async def main() -> None:
    # Get a reference to the event loop as we plan to use low-level APIs.
    loop = asyncio.get_running_loop()

    on_con_lost = loop.create_future()
    message = "Hello World!"
    transport, _ = await loop.create_datagram_endpoint(
        lambda: EchoClientProtocol(message, on_con_lost),
        remote_addr=('127.0.0.1', 9999))

    try:
        await on_con_lost
    finally:
        transport.close()

if __name__ == '__main__':
    asyncio.run(main())
