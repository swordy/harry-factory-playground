"""
Data Validation Gate - Main application module
Provides automated validation mechanisms for incoming data covering:
- Format validation
- Type checking
- Business constraint enforcement
- Comprehensive error handling
"""

from flask import Flask, request, jsonify
from validators import validate_user_data, ValidationError
from typing import Dict, Any

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy"}), 200


@app.route('/validate', methods=['POST'])
def validate():
    """
    Data validation endpoint
    Accepts JSON payload and validates against defined constraints
    Returns validation results with detailed error messages
    """
    try:
        # Parse incoming JSON - handle missing or invalid JSON
        try:
            data = request.get_json(force=True, silent=False)
        except Exception:
            # If JSON parsing fails, treat as missing payload
            data = None

        if data is None:
            return jsonify({
                "valid": False,
                "errors": ["No JSON payload provided"]
            }), 400

        # Validate the data
        result = validate_user_data(data)

        # Return validation result
        return jsonify(result), 200 if result["valid"] else 400

    except ValidationError as ve:
        return jsonify({
            "valid": False,
            "errors": [str(ve)]
        }), 400
    except Exception as e:
        return jsonify({
            "valid": False,
            "errors": [f"Validation error: {str(e)}"]
        }), 500


@app.errorhandler(400)
def bad_request(error):
    """Handle bad request errors"""
    return jsonify({
        "valid": False,
        "errors": ["Invalid request"]
    }), 400


@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors"""
    return jsonify({
        "valid": False,
        "errors": ["Internal server error"]
    }), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
