import http.client
import json
import subprocess
import os

def spawn_new_process(command):
    try:
        # Spawn a new process
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Wait for the process to finish and get the output
        stdout, stderr = process.communicate()

        # Print the output
        print("STDOUT:")
        print(stdout.decode('utf-8'))
        print("STDERR:")
        print(stderr.decode('utf-8'))

    except Exception as e:
        print("Error:", e)

def send_json_message(message):
    try:
        # Create a connection to the local HTTP server (localhost)
        conn = http.client.HTTPConnection("localhost", 8000)  # Replace 8000 with the port your server is running on

        # Prepare the JSON message
        data = json.dumps({'message': message})

        # Set headers
        headers = {'Content-type': 'application/json'}

        # Send a POST request with JSON data
        conn.request("POST", "/", data, headers)

        # Get the response from the server
        response = conn.getresponse()

        # Print the response status code and body
        print("Response Status:", response.status)

        if (response.status == 200) :
            current_folder = os.getcwd()

            output_response = response.read().decode('utf-8');
            
            command = current_folder + "/test " + output_response
            
            spawn_new_process(command)

        print("Response Body:")
        print(response.read().decode('utf-8'))  # Decode the response body bytes to a string

    except ConnectionRefusedError:
        print("Connection refused. Make sure the HTTP server is running on localhost:8000.")

if __name__ == "__main__":
    message = input("Enter a message to send to the server: ")
    send_json_message(message)
