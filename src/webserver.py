import os
import http.server as server
from lgl_post import send_all_data
from datetime import datetime

os.chdir('.')

def delete_local_file(path):
    if os.path.exists(path):
        os.remove(path)

class HTTPRequestHandler(server.SimpleHTTPRequestHandler):
    """Extend SimpleHTTPRequestHandler to handle PUT requests"""
    def do_POST(self):
        file_length = int(self.headers['Content-Length'])
        now = datetime.now()
        filename = str(now) + "_uploaded_file.csv"
        with open(filename, 'wb') as output_file:
            output_file.write(self.rfile.read(file_length))
        self.send_response(201, 'Created')
        
        send_all_data(filename)
        delete_local_file(filename)
        self.end_headers()
        reply_body = 'Saved Upload"%s"\n'
        self.wfile.write(reply_body.encode('utf-8'))


# # Create server object listening the port 80  --int(os.environ['PORT'])
server_object = server.HTTPServer(server_address=('0.0.0.0', int(os.environ['PORT'])), RequestHandlerClass=HTTPRequestHandler)

# # Start the web server
server_object.serve_forever()