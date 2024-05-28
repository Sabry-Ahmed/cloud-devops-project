from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data
data = {
    "message": "test"
}

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def post_data():
    new_data = request.json
    data.update(new_data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
