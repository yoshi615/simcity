from flask import Flask, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # CORSを有効にする

@app.route('/execute')
def execute_script():
    result = subprocess.run(['python', 'execute_all.py'], capture_output=True, text=True)
    return jsonify(output=result.stdout)

if __name__ == '__main__':
    app.run(debug=True)