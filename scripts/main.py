import os
from generate_code import generate_code
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open('../templates/index.html', 'r') as file:
                self.wfile.write(file.read().encode())
        elif self.path == '/generate':
            # Your code generation logic here
            with open('../static/style.css', 'r') as file:
                self.wfile.write(file.read().encode())
        else:
            self.send_error(404)


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if not os.path.exists('../codes'):
        os.makedirs('../codes')

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()