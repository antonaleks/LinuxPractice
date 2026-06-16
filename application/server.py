from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/get':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'GET OK')

    def do_POST(self):
        if self.path == '/post':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'POST OK')

    def do_PUT(self):
        if self.path == '/put':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'PUT OK')

HTTPServer(('0.0.0.0', 5000), Handler).serve_forever()