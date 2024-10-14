#!/usr/bin/env python
"""
UDP Echo Server <https://docs.python.org/3/library/asyncio-protocol.html>

A UDP echo server, using the ``loop.create_datagram_endpoint()`` method, sends
back received data
"""

import asyncio
from typing import Any, Self

class EchoServerProtocol(asyncio.DatagramProtocol):
    def connection_made(
            self: Self,
            transport: asyncio.BaseTransport) -> None:
        assert(isinstance(transport, asyncio.DatagramTransport))
        self.transport = transport

    def datagram_received(
            self: Self,
            data: bytes,
            addr: Any) -> None:
        message = data.decode()
        print(f'Received {message!r} from {addr}')
        print(f'Send {message!r} to {addr}', flush=True)
        self.transport.sendto(data, addr)

async def main() -> None:
    print("Starting UDP server", flush=True)

    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()

    # One protocol instance will be created to serve all client requests
    transport, _ = await loop.create_datagram_endpoint(
        lambda: EchoServerProtocol(),
        local_addr=('127.0.0.1', 9999))

    try:
        await asyncio.sleep(3600)
    finally:
        transport.close()

if __name__ == '__main__':
    asyncio.run(main())
