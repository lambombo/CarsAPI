from flask import jsonify, request

from . import status

# Register API routes
@status.route('/', methods=['GET'])
def main():
    data = {"status":"ok"}
    if request.method == 'GET':
        return jsonify(data=data), 200
    return jsonify(data=data), 200
