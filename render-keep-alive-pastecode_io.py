import threading
import requests
from time import sleep
from flask import Flask, jsonify

app = Flask(__name__)

health_thread = None

def health_loop():
    while True:
        # Make a request to the health endpoint
        response = requests.get('https://placeholder-url.com/health')
        
        # Check the response status code
        if response.status_code == 200:
            print('Server up and running')
        else:
            print('Server down or not reachable')
        
        # Wait for 13 minutes before making the next request
        sleep(13 * 60)

def start_health_check():
    global health_thread
    if not health_thread or not health_thread.is_alive():
        health_thread = threading.Thread(target=health_loop)
        health_thread.start()

# Start the health check upon Flask deployment
start_health_check()

# Health route
@app.route('/health', methods=['GET'])
def health_check():
    # Check if your application is healthy
    health_status = {'status': 'ok'}
    return jsonify(health_status), 200
