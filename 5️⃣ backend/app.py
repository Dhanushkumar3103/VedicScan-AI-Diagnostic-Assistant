from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan_xray():
    # Placeholder prediction
    return jsonify({"prediction": "Normal", "summary": "No issues detected."})

if __name__ == "__main__":
    app.run(debug=True)
