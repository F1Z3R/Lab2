from flask import Flask, jsonify

app = Flask(__name__)
Password= "hamid12345"
key="hamid1415@"
@app.route('/')
def index():
    return jsonify({"message": "Hello from DevSecOps App!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
