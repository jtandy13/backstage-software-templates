import os
from flask import Flask, jsonify
from flask_cors import CORS
import datetime
import socket

app = Flask(__name__)

# Allow Backstage frontend origins; configurable per environment
cors_origins = os.environ.get(
    'CORS_ORIGINS',
    'http://localhost:3000',
).split(',')

CORS(app, origins=cors_origins, supports_credentials=False)

@app.route('/')
def health_check():
    return {"status": "healthy"}, 200

@app.route('/api/v1/info')
def info():
    return jsonify({
        'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'hostname': socket.gethostname(),
        'message': 'This is the details page!',
        'deployed_on': 'kubernetes',
        'env': '${{ values.app_env }}',
        'app_name': '${{ values.app_name }}'
    })

@app.route('/api/v1/healthz')
def healthz():
    return jsonify({'status': 'up'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')


# '/api/v1/details'
# '/api/v1/healthz'