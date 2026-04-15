from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)
SECRET_KEY = "mysecret"

def authenticate(token):
    """Validates JWT token and returns user payload"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

@app.route('/api/users', methods=['GET'])
def get_users():
    """Returns list of all users - requires auth"""
    token = request.headers.get('Authorization')
    if not authenticate(token):
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify({"users": ["sai", "admin"]})

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint - no auth required"""
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(debug=True)
