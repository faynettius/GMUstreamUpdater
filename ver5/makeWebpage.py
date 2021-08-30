# server.py
import http.server # Our http server handler for http requests
import socketserver # Establish the TCP Socket connections
import socket
import sys

# port = int(input("Input Port (1025-9999):"))
port = int(sys.argv[1])
if port < 1024 or port > 9999:
    raise Exception("Please input a port between 1025 and 9999")
print(port)
myip = socket.gethostbyname(socket.gethostname()) # The local IP for this computer

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = 'stream_elements.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyHttpRequestHandler

with socketserver.TCPServer(("", port), Handler) as httpd:
    print(f"Http Server Serving at {myip}:{port}")
    httpd.serve_forever()
