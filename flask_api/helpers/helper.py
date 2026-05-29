from flask import jsonify


def success(data=None):
    return jsonify({
        "success": True,
        "data": data
    })


def fail(message=None, code=400, data=None):
    return jsonify({
        "success": False,
        "message": message,
        "data": data
    }), code