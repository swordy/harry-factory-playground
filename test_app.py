"""
Integration tests for the Flask API
Tests the validation endpoint and error handling
"""

import pytest
import json
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestHealthEndpoint:
    """Test the health check endpoint"""

    def test_health_endpoint(self, client):
        """Test health check returns 200"""
        response = client.get('/health')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['status'] == 'healthy'


class TestValidateEndpoint:
    """Test the validation endpoint"""

    def test_validate_valid_data(self, client):
        """Test validation with valid data"""
        valid_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "age": 25,
            "phone": "1234567890",
            "password": "StrongPass1!"
        }
        response = client.post(
            '/validate',
            data=json.dumps(valid_data),
            content_type='application/json'
        )
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['valid'] is True
        assert len(data['errors']) == 0

    def test_validate_missing_fields(self, client):
        """Test validation with missing required fields"""
        invalid_data = {
            "name": "John Doe",
            "email": "john@example.com"
        }
        response = client.post(
            '/validate',
            data=json.dumps(invalid_data),
            content_type='application/json'
        )
        assert response.status_code == 400
        data = json.loads(response.data)
        assert data['valid'] is False
        assert len(data['errors']) > 0

    def test_validate_invalid_email(self, client):
        """Test validation with invalid email"""
        invalid_data = {
            "name": "John Doe",
            "email": "invalid-email",
            "age": 25,
            "phone": "1234567890",
            "password": "StrongPass1!"
        }
        response = client.post(
            '/validate',
            data=json.dumps(invalid_data),
            content_type='application/json'
        )
        assert response.status_code == 400
        data = json.loads(response.data)
        assert data['valid'] is False
        assert any('email' in error.lower() for error in data['errors'])

    def test_validate_invalid_age(self, client):
        """Test validation with invalid age"""
        invalid_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "age": 200,
            "phone": "1234567890",
            "password": "StrongPass1!"
        }
        response = client.post(
            '/validate',
            data=json.dumps(invalid_data),
            content_type='application/json'
        )
        assert response.status_code == 400
        data = json.loads(response.data)
        assert data['valid'] is False

    def test_validate_invalid_phone(self, client):
        """Test validation with invalid phone"""
        invalid_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "age": 25,
            "phone": "123",
            "password": "StrongPass1!"
        }
        response = client.post(
            '/validate',
            data=json.dumps(invalid_data),
            content_type='application/json'
        )
        assert response.status_code == 400
        data = json.loads(response.data)
        assert data['valid'] is False

    def test_validate_weak_password(self, client):
        """Test validation with weak password"""
        invalid_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "age": 25,
            "phone": "1234567890",
            "password": "weak"
        }
        response = client.post(
            '/validate',
            data=json.dumps(invalid_data),
            content_type='application/json'
        )
        assert response.status_code == 400
        data = json.loads(response.data)
        assert data['valid'] is False

    def test_validate_no_json_payload(self, client):
        """Test validation with no JSON payload"""
        response = client.post('/validate')
        assert response.status_code == 400
        data = json.loads(response.data)
        assert data['valid'] is False

    def test_validate_age_under_18_business_rule(self, client):
        """Test business rule: user must be at least 18"""
        invalid_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "age": 16,
            "phone": "1234567890",
            "password": "StrongPass1!"
        }
        response = client.post(
            '/validate',
            data=json.dumps(invalid_data),
            content_type='application/json'
        )
        assert response.status_code == 400
        data = json.loads(response.data)
        assert data['valid'] is False
        assert any('18' in error for error in data['errors'])

    def test_validate_invalid_name_characters(self, client):
        """Test validation with invalid characters in name"""
        invalid_data = {
            "name": "John123",
            "email": "john@example.com",
            "age": 25,
            "phone": "1234567890",
            "password": "StrongPass1!"
        }
        response = client.post(
            '/validate',
            data=json.dumps(invalid_data),
            content_type='application/json'
        )
        assert response.status_code == 400
        data = json.loads(response.data)
        assert data['valid'] is False

    def test_validate_multiple_errors(self, client):
        """Test that multiple validation errors are reported"""
        invalid_data = {
            "name": "123Invalid",
            "email": "invalid-email",
            "age": 200,
            "phone": "123",
            "password": "weak"
        }
        response = client.post(
            '/validate',
            data=json.dumps(invalid_data),
            content_type='application/json'
        )
        assert response.status_code == 400
        data = json.loads(response.data)
        assert data['valid'] is False
        assert len(data['errors']) > 2

    def test_validate_sanitized_input(self, client):
        """Test that whitespace is properly sanitized"""
        data = {
            "name": "  John Doe  ",
            "email": "  john@example.com  ",
            "age": 25,
            "phone": "1234567890",
            "password": "StrongPass1!"
        }
        response = client.post(
            '/validate',
            data=json.dumps(data),
            content_type='application/json'
        )
        assert response.status_code == 200
        result = json.loads(response.data)
        assert result['valid'] is True

    def test_validate_edge_case_age_18(self, client):
        """Test edge case: age exactly 18 should pass"""
        data = {
            "name": "John Doe",
            "email": "john@example.com",
            "age": 18,
            "phone": "1234567890",
            "password": "StrongPass1!"
        }
        response = client.post(
            '/validate',
            data=json.dumps(data),
            content_type='application/json'
        )
        assert response.status_code == 200
        result = json.loads(response.data)
        assert result['valid'] is True

    def test_validate_edge_case_age_0(self, client):
        """Test edge case: age 0 should fail business rule"""
        data = {
            "name": "John Doe",
            "email": "john@example.com",
            "age": 0,
            "phone": "1234567890",
            "password": "StrongPass1!"
        }
        response = client.post(
            '/validate',
            data=json.dumps(data),
            content_type='application/json'
        )
        assert response.status_code == 400
        result = json.loads(response.data)
        assert result['valid'] is False

    def test_validate_special_characters_in_name(self, client):
        """Test name with allowed special characters"""
        data = {
            "name": "Jean-Paul O'Brien",
            "email": "jean@example.com",
            "age": 30,
            "phone": "1234567890",
            "password": "StrongPass1!"
        }
        response = client.post(
            '/validate',
            data=json.dumps(data),
            content_type='application/json'
        )
        assert response.status_code == 200
        result = json.loads(response.data)
        assert result['valid'] is True


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
