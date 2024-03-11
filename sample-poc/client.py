import http.client

def access_local_http_server():
    try:
        # Create a connection to the local HTTP server (localhost)
        conn = http.client.HTTPConnection("localhost", 8000)  # Replace 8000 with the port your server is running on

        # Send a GET request to the root URL
        conn.request("GET", "/")

        # Get the response from the server
        response = conn.getresponse()

        # Print the response status code and body
        print("Response Status:", response.status)
        print("Response Body:")
        print(response.read().decode('utf-8'))  # Decode the response body bytes to a string

    except ConnectionRefusedError:
        print("Connection refused. Make sure the HTTP server is running on localhost:8000.")

if __name__ == "__main__":
    access_local_http_server()
