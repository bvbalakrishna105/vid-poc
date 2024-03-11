from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Define the HTTP request handler class
class RequestHandler(BaseHTTPRequestHandler):
    # HTTP GET method handler
    def do_GET(self):
        # Set response status code
        self.send_response(200)
        
        # Set response headers
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # Send a JSON response
        response = {'message': 'This is the server response!'}
        self.wfile.write(json.dumps(response).encode('utf-8'))

    # HTTP POST method handler
    def do_POST(self):
        # Get the length of the incoming request body
        content_length = int(self.headers['Content-Length'])
        
        # Read the incoming request data
        post_data = self.rfile.read(content_length)
        
        # Parse the JSON data
        request = json.loads(post_data.decode('utf-8'))
        
        # Process the request and prepare response
        response = {'received_message': request['message'], 'response': 'Thanks for your message!'}
        
        # Set response status code
        self.send_response(200)
        
        # Set response headers
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # Send a JSON response
        self.wfile.write(json.dumps(response).encode('utf-8'))

# Define the main function
def main():
    try:
        # Create an HTTP server listening on port 8000
        server_address = ('', 8000)
        httpd = HTTPServer(server_address, RequestHandler)
        
        # Print a message indicating the server is running
        print('Server running on port 8000...')
        
        # Start the HTTP server
        httpd.serve_forever()

    except KeyboardInterrupt:
        # If Ctrl+C is pressed, stop the server
        print('Stopping server...')
        httpd.socket.close()

# Run the main function if the script is executed directly
if __name__ == '__main__':
    main()
