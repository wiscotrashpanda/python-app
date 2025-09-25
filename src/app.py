from flask import Flask, jsonify
import datetime
import socket
import pytz

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    cdt = pytz.timezone('America/Chicago')
    now_cdt = datetime.datetime.now(cdt)
    return jsonify({
        "time": now_cdt.isoformat(),
        "hostname": socket.gethostname()
    })

@app.route('/api/v1/healthz')
def healthz():
    return jsonify({
        'status': 'ok'
    }), 200

if __name__ == '__main__':
    app.run()
