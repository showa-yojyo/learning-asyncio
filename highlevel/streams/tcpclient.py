#!/usr/bin/env python

"""
Streams <https://docs.python.org/3/library/asyncio-stream.html>

Assume that tcpserver.py is running in another console.
"""

import asyncio

async def tcp_echo_client(message: str) -> None:
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

if __name__ == '__main__':
    asyncio.run(tcp_echo_client('Hello World!'))
