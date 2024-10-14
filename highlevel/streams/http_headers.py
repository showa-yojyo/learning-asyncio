#!/usr/bin/env python

"""
Streams <https://docs.python.org/3/library/asyncio-stream.html>

Usage:

$ ./http_headers.py http://example.com/path/page.html
$ ./http_headers.py https://example.com/path/page.html

Features:
- asyncio.open_connection()
- asyncio.run()
- urllib.parse.urlsplit()
"""

import asyncio
import urllib.parse
import sys

async def print_http_headers(url):
    url = urllib.parse.urlsplit(url)
    if url.scheme == 'https':
        reader, writer = await asyncio.open_connection(
            url.hostname, 443, ssl=True)
    else:
        reader, writer = await asyncio.open_connection(
            url.hostname, 80)

    query = (
        f"HEAD {url.path or '/'} HTTP/1.0\r\n"
        f"Host: {url.hostname}\r\n"
        f"\r\n"
    )

    writer.write(query.encode('latin-1'))
    while True:
        line = await reader.readline()
        if not line:
            break

        if text := line.decode('latin-1').rstrip():
            print(f'HTTP header> {text}')

    # Ignore the body, close the socket
    writer.close()
    await writer.wait_closed()

if __name__ == '__main__':
    # コメント： http://example.com/ で十分
    url = sys.argv[1]
    asyncio.run(print_http_headers(url))
