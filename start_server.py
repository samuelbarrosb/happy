import http.server
import socketserver
import threading
import os

PORT = 8000
DIRECTORY = "e:/Clientes/Happy/happy"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

t = threading.Thread(target=start_server, daemon=True)
t.start()

import time
time.sleep(2)
print("Server started on port 8000")
