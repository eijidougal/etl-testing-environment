from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data to be returned by the API
SAMPLE_DATA = [
    {"id": 1, "name": "Item 1", "value": 100},
    {"id": 2, "name": "Item 2", "value": 200},
    {"id": 3, "name": "Item 3", "value": 300},
    {"id": 4, "name": "Item 4", "value": 400},
    {"id": 5, "name": "Item 5", "value": 500},
]


# Endpoint to get data
@app.route('/data', methods=['GET'])
def get_data():
    """
    Returns a subset of the sample data based on the 'limit' query parameter.
    """
    # Get the 'limit' query parameter if provided
    limit = request.args.get('limit', default=5, type=int)

    # Slice the sample data based on the limit (to simulate pagination or limits)
    limited_data = SAMPLE_DATA[:limit]

    return jsonify({"results": limited_data})


# Endpoint to get a specific item by ID
@app.route('/data/<int:item_id>', methods=['GET'])
def get_data_by_id(item_id):
    """
    Returns a specific item from the sample data based on the provided item_id.
    """
    # Filter the data for the specific item_id
    item = next((item for item in SAMPLE_DATA if item["id"] == item_id), None)

    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404


# Endpoint to simulate a POST request (e.g., for creating a new item)
@app.route('/data', methods=['POST'])
def create_data():
    """
    Simulates adding a new item to the data.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid data"}), 400

    new_item = {
        "id": len(SAMPLE_DATA) + 1,
        "name": data.get("name"),
        "value": data.get("value")
    }
    SAMPLE_DATA.append(new_item)

    return jsonify(new_item), 201


# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
