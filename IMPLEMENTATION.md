# Data Validation Gate - Implementation

## Overview

This is a comprehensive implementation of a Data Validation Gate system that provides automated validation mechanisms for incoming data. The system covers formats, types, business constraints, and comprehensive error handling.

## Architecture

### Module Structure

1. **app.py** - Flask API with two endpoints:
   - `/health` - Health check endpoint
   - `/validate` - Data validation endpoint

2. **validators.py** - Core validation logic:
   - Input sanitization
   - Format validation (email, phone, etc.)
   - Type checking
   - Business constraint enforcement
   - Comprehensive error handling

3. **test_validators.py** - Unit tests for validation functions
4. **test_app.py** - Integration tests for API endpoints

## Features Implemented

### ✅ Input Sanitization
- Whitespace trimming
- UTF-8 encoding validation
- Prevention of injection attacks

### ✅ Type Checking
- Validates data types for all required fields
- Enforces strict type requirements (e.g., age must be integer)
- Clear error messages for type mismatches

### ✅ Format Validation
- **Email**: Standard email format using regex
- **Phone**: International and domestic format support
- **Name**: Alphanumeric with allowed special characters (hyphens, apostrophes)
- **Password**: Strong password requirements (8+ chars, uppercase, lowercase, digit, special char)

### ✅ Business Constraint Enforcement
- **Age constraint**: Users must be at least 18 years old
- **Age range**: Must be between 0-150
- **Name length**: 1-100 characters
- **Required fields**: All specified fields are mandatory

### ✅ Error Handling
- Comprehensive error messages
- Multiple errors reported in single validation
- Proper HTTP status codes (200 for valid, 400 for invalid, 500 for errors)
- JSON error response format

## API Endpoints

### GET /health
Health check endpoint.

**Response:**
```json
{
  "status": "healthy"
}
```

### POST /validate
Validates user data against defined constraints.

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "age": 25,
  "phone": "1234567890",
  "password": "StrongPass1!"
}
```

**Response (Valid):**
```json
{
  "valid": true,
  "errors": [],
  "data": {...}
}
```

**Response (Invalid):**
```json
{
  "valid": false,
  "errors": [
    "'email' format is invalid",
    "'password' validation failed: ..."
  ]
}
```

## Validation Rules

### Name
- Required field
- String type
- 1-100 characters
- Letters, spaces, hyphens, and apostrophes only

### Email
- Required field
- Valid email format (standard pattern)
- Example: user@example.com

### Age
- Required field
- Integer type
- 0-150 range
- Business rule: Must be >= 18 years old

### Phone
- Required field
- String type
- 7-15 digits
- Supports international format (+1-123-456-7890)
- Removes separators automatically

### Password
- Required field
- String type
- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character

## Test Coverage

### Unit Tests (32 tests)
- String sanitization (4 tests)
- Email validation (3 tests)
- Age validation (3 tests)
- Phone validation (3 tests)
- Password validation (7 tests)
- Complete user data validation (12 tests)

### Integration Tests (15 tests)
- Health endpoint
- Valid data validation
- Missing required fields
- Invalid formats
- Edge cases (age exactly 18, age 0)
- Special characters in names
- Multiple validation errors
- Error handling

**Total: 47 tests - All passing ✅**

## Running the Application

### Installation
```bash
pip install -r requirements.txt
```

### Running Tests
```bash
pytest test_validators.py test_app.py -v
```

### Running the API
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## Example Usage

### Valid Request
```bash
curl -X POST http://localhost:5000/validate \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "age": 25,
    "phone": "1234567890",
    "password": "StrongPass1!"
  }'
```

### Invalid Request (Age < 18)
```bash
curl -X POST http://localhost:5000/validate \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jane Doe",
    "email": "jane@example.com",
    "age": 16,
    "phone": "1234567890",
    "password": "StrongPass1!"
  }'
```

Response:
```json
{
  "valid": false,
  "errors": ["Business rule: User must be at least 18 years old"]
}
```

## Security Considerations

1. **Input Sanitization**: All string inputs are sanitized to prevent injection attacks
2. **Type Validation**: Strict type checking prevents type confusion attacks
3. **Format Validation**: Regex patterns prevent malformed data
4. **Business Rules**: Age constraint ensures compliance with regulations
5. **Error Messages**: Detailed but safe error messages for debugging

## Code Quality

- Clear separation of concerns (validation logic vs. API)
- Comprehensive docstrings
- Meaningful variable and function names
- Proper error handling and propagation
- Extensible design for adding new validation rules
