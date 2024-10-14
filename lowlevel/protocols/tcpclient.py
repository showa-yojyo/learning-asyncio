#!/usr/bin/env python
"""
TCP Echo Client <https://docs.python.org/3/library/asyncio-protocol.html>

A TCP echo client using the ``loop.create_connection()`` method, sends data, and
waits until the connection is closed:
"""

import asyncio
from typing import Self

class EchoClientProtocol(asyncio.Protocol):
    def __init__(
            self: Self,
            message: str,
            on_con_lost: asyncio.Future) -> None:
        super().__init__()
        self.message = message
        self.on_con_lost = on_con_lost

    def connection_made(
            self: Self,
            transport: asyncio.BaseTransport) -> None:
        assert(isinstance(transport, asyncio.WriteTransport))
        transport.write(self.message.encode())
        print(f'Data sent: {self.message!r}')

    def data_received(
            self: Self,
            data: bytes) -> None:
        print(f'Data received: {data.decode()!r}')

    def connection_lost(
            self: Self,
            _: Exception | None) -> None:
        print('The server closed the connection')
        self.on_con_lost.set_result(True)

async def main() -> None:
    # Get a reference to the event loop as we plan to use low-level APIs.
    loop = asyncio.get_running_loop()

    on_con_lost = loop.create_future()
    message = 'Hello World!'

    transport, _ = await loop.create_connection(
        lambda: EchoClientProtocol(message, on_con_lost),
        '127.0.0.1', 8888)

    # Wait until the protocol signals that the connection is lost and close the
    # transport.
    try:
        await on_con_lost
    finally:
        transport.close()

if __name__ == '__main__':
    asyncio.run(main())
