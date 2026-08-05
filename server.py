#!/usr/bin/env python3
import argparse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

class Handler(SimpleHTTPRequestHandler):
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        '.wav': 'audio/wav',
        '.json': 'application/json; charset=utf-8',
        '.js': 'application/javascript; charset=utf-8',
        '.css': 'text/css; charset=utf-8',
    }

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('--port', type=int, default=8898)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    import os
    os.chdir(root)
    httpd = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f'Serving {root} at http://{args.host}:{args.port}/')
    httpd.serve_forever()
