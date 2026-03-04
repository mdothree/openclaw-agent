#!/usr/bin/env python3
"""
OpenClaw Agent

General purpose search/research agent
"""

import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

PORT = int(os.environ.get("PORT", 10000))


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        response = {
            "service": "openclaw",
            "status": "running",
            "message": "General purpose search/research agent"
        }
        self.wfile.write(json.dumps(response).encode())

    def log_message(self, format, *args):
        print(f"[openclaw] {args[0]}")


if __name__ == "__main__":
    print(f"Starting openclaw on port {PORT}")
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    server.serve_forever()
