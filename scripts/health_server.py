#!/usr/bin/env python3
"""Local observe-only health. Bind 127.0.0.1. No vendor."""

from __future__ import annotations

import json
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from health import health  # noqa: E402

HOST = "127.0.0.1"
PORT = 8787


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path.rstrip("/") not in {"", "/", "/health"}:
            self.send_error(404)
            return
        body = json.dumps(health()).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt: str, *args: object) -> None:
        return


def main() -> None:
    httpd = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"health {HOST}:{PORT}")
    httpd.serve_forever()


if __name__ == "__main__":
    main()
