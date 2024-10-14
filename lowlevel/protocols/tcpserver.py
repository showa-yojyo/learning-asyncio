#!/usr/bin/env python
"""
TCP Echo Server <https://docs.python.org/3/library/asyncio-protocol.html>

Create a TCP echo server using the ``loop.create_server()`` method, send back
received data, and close the connection
"""
import asyncio
from typing import Self

class EchoServerProtocol(asyncio.Protocol):
    def connection_made(
            self: Self,
            transport: asyncio.BaseTransport) -> None:
        peername = transport.get_extra_info('peername')
        print(f'Connection from {peername}', flush=True)
        self.transport = transport

    def data_received(self: Self, data: bytes) -> None:
        message = data.decode()
        print(f'Data received: {message!r}')

        print(f'Send: {message!r}')
        assert(isinstance(self.transport, asyncio.WriteTransport))
        self.transport.write(data)

        print('Close the client socket', flush=True)
        self.transport.close()

async def main() -> None:
    # Get a reference to the event loop as we plan to use low-level APIs.
    loop = asyncio.get_running_loop()

    # Each client connection will create a new protocol instance
    server = await loop.create_server(
        lambda: EchoServerProtocol(),
        '127.0.0.1', 8888)

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
