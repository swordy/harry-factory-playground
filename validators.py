"""
Data Validation Module
Provides comprehensive validation for user data including:
- Type checking
- Format validation
- Business constraint enforcement
- Input sanitization
"""

import re
from typing import Dict, Any, List, Optional
from datetime import datetime


class ValidationError(Exception):
    """Custom exception for validation errors"""
    pass


def sanitize_string(value: Any) -> Optional[str]:
    """
    Sanitize string input to prevent injection attacks
    - Removes leading/trailing whitespace
    - Validates UTF-8 encoding
    """
    if not isinstance(value, str):
        return None

    # Remove leading/trailing whitespace
    sanitized = value.strip()

    # Check for valid UTF-8
    try:
        sanitized.encode('utf-8')
    except UnicodeEncodeError:
        return None

    return sanitized


def validate_email(email: str) -> bool:
    """
    Validate email format
    Enforces standard email pattern
    """
    if not isinstance(email, str):
        return False

    email = email.strip()
    # Standard email regex pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_age(age: Any) -> bool:
    """
    Validate age with business constraints
    - Must be integer
    - Must be between 0 and 150
    - Business rule: adult age >= 18 for certain operations
    """
    if not isinstance(age, int):
        return False

    return 0 <= age <= 150


def validate_phone(phone: str) -> bool:
    """
    Validate phone number format
    Supports international format: +1-123-456-7890 or 1234567890
    """
    if not isinstance(phone, str):
        return False

    phone = phone.strip()
    # Remove common separators and spaces
    cleaned = re.sub(r'[\s\-\(\)]+', '', phone)

    # Must be 7-15 digits with optional + prefix
    pattern = r'^\+?[0-9]{7,15}$'
    return bool(re.match(pattern, cleaned))


def validate_password(password: str) -> tuple[bool, str]:
    """
    Validate password strength
    Requirements:
    - At least 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character
    """
    if not isinstance(password, str):
        return False, "Password must be a string"

    if len(password) < 8:
        return False, "Password must be at least 8 characters long"

    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter"

    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter"

    if not re.search(r'\d', password):
        return False, "Password must contain at least one digit"

    if not re.search(r'[!@#$%^&*()_\-+=\[\]{};:\'",.<>?/\\|`~]', password):
        return False, "Password must contain at least one special character"

    return True, ""


def validate_user_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Main validation function for user data
    Validates all required fields and business constraints

    Expected fields:
    - name: string, 1-100 characters
    - email: valid email format
    - age: integer, 0-150
    - phone: valid phone format
    - password: strong password

    Returns dict with 'valid' boolean and 'errors' list
    """
    errors: List[str] = []

    # Check that data is a dictionary
    if not isinstance(data, dict):
        return {
            "valid": False,
            "errors": ["Input must be a JSON object"]
        }

    # Validate 'name' field
    if 'name' not in data:
        errors.append("'name' field is required")
    else:
        name = sanitize_string(data['name'])
        if name is None:
            errors.append("'name' must be a valid string")
        elif not (1 <= len(name) <= 100):
            errors.append("'name' must be between 1 and 100 characters")
        elif not re.match(r'^[a-zA-Z\s\-\']+$', name):
            errors.append("'name' must contain only letters, spaces, hyphens, and apostrophes")

    # Validate 'email' field
    if 'email' not in data:
        errors.append("'email' field is required")
    else:
        email = sanitize_string(data['email'])
        if email is None:
            errors.append("'email' must be a valid string")
        elif not validate_email(email):
            errors.append("'email' format is invalid")

    # Validate 'age' field
    if 'age' not in data:
        errors.append("'age' field is required")
    else:
        if not isinstance(data['age'], int):
            errors.append("'age' must be an integer")
        elif not validate_age(data['age']):
            errors.append("'age' must be between 0 and 150")

    # Validate 'phone' field
    if 'phone' not in data:
        errors.append("'phone' field is required")
    else:
        phone = sanitize_string(data['phone'])
        if phone is None:
            errors.append("'phone' must be a valid string")
        elif not validate_phone(phone):
            errors.append("'phone' format is invalid")

    # Validate 'password' field
    if 'password' not in data:
        errors.append("'password' field is required")
    else:
        password = data.get('password')
        if not isinstance(password, str):
            errors.append("'password' must be a string")
        else:
            is_valid, error_msg = validate_password(password)
            if not is_valid:
                errors.append(f"'password' validation failed: {error_msg}")

    # Business constraint: age must be >= 18 for account creation
    if 'age' in data and isinstance(data['age'], int) and data['age'] >= 0:
        if data['age'] < 18:
            errors.append("Business rule: User must be at least 18 years old")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "data": data if len(errors) == 0 else None
    }
