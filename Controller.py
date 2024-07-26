from flask import request, jsonify
import service

def register_routes(app):
    @app.route('/getitems', methods=['GET'])
    def get_items():
        items = service.get_all_items()
        return jsonify(items)

    @app.route('/additems', methods=['POST'])
    def add_item():
        data = request.json
        inserted_id = service.add_item(data)
        return jsonify({"inserted_id": inserted_id}), 201

    """@app.route('/putitems',methods=['PUT'])
    def modify_item():
        data"""






