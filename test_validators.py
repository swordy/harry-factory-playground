"""
Unit tests for the validators module
Tests all validation functions and business rules
"""

import pytest
from validators import (
    validate_user_data, validate_email, validate_age,
    validate_phone, validate_password, sanitize_string,
    ValidationError
)


class TestSanitizeString:
    """Test string sanitization"""

    def test_sanitize_basic_string(self):
        """Test sanitizing a basic string"""
        result = sanitize_string("  hello  ")
        assert result == "hello"

    def test_sanitize_non_string(self):
        """Test sanitizing non-string input"""
        assert sanitize_string(123) is None
        assert sanitize_string(None) is None
        assert sanitize_string([]) is None

    def test_sanitize_valid_utf8(self):
        """Test sanitizing valid UTF-8 string"""
        result = sanitize_string("café")
        assert result == "café"

    def test_sanitize_empty_string(self):
        """Test sanitizing empty string"""
        result = sanitize_string("")
        assert result == ""


class TestValidateEmail:
    """Test email validation"""

    def test_valid_email(self):
        """Test valid email formats"""
        assert validate_email("user@example.com") is True
        assert validate_email("john.doe@company.co.uk") is True
        assert validate_email("test+tag@domain.org") is True

    def test_invalid_email(self):
        """Test invalid email formats"""
        assert validate_email("invalid.email") is False
        assert validate_email("@example.com") is False
        assert validate_email("user@") is False
        assert validate_email("user name@example.com") is False

    def test_email_non_string(self):
        """Test email validation with non-string input"""
        assert validate_email(123) is False
        assert validate_email(None) is False


class TestValidateAge:
    """Test age validation"""

    def test_valid_age(self):
        """Test valid ages"""
        assert validate_age(25) is True
        assert validate_age(0) is True
        assert validate_age(150) is True
        assert validate_age(18) is True

    def test_invalid_age(self):
        """Test invalid ages"""
        assert validate_age(-1) is False
        assert validate_age(151) is False
        assert validate_age(200) is False

    def test_age_non_integer(self):
        """Test age validation with non-integer input"""
        assert validate_age("25") is False
        assert validate_age(25.5) is False
        assert validate_age(None) is False


class TestValidatePhone:
    """Test phone number validation"""

    def test_valid_phone_formats(self):
        """Test valid phone number formats"""
        assert validate_phone("1234567890") is True
        assert validate_phone("+1-123-456-7890") is True
        assert validate_phone("+33123456789") is True
        assert validate_phone("(123) 456-7890") is True
        assert validate_phone("+1 (123) 456-7890") is True

    def test_invalid_phone_formats(self):
        """Test invalid phone number formats"""
        assert validate_phone("12345") is False  # Too short
        assert validate_phone("abc-def-ghij") is False  # Non-numeric
        assert validate_phone("") is False

    def test_phone_non_string(self):
        """Test phone validation with non-string input"""
        assert validate_phone(1234567890) is False
        assert validate_phone(None) is False


class TestValidatePassword:
    """Test password validation"""

    def test_valid_password(self):
        """Test valid password formats"""
        is_valid, msg = validate_password("StrongPass1!")
        assert is_valid is True
        assert msg == ""

        is_valid, msg = validate_password("MyP@ssw0rd")
        assert is_valid is True

    def test_password_too_short(self):
        """Test password too short"""
        is_valid, msg = validate_password("Short1!")
        assert is_valid is False
        assert "at least 8 characters" in msg

    def test_password_no_uppercase(self):
        """Test password without uppercase letter"""
        is_valid, msg = validate_password("mypassword1!")
        assert is_valid is False
        assert "uppercase" in msg

    def test_password_no_lowercase(self):
        """Test password without lowercase letter"""
        is_valid, msg = validate_password("MYPASSWORD1!")
        assert is_valid is False
        assert "lowercase" in msg

    def test_password_no_digit(self):
        """Test password without digit"""
        is_valid, msg = validate_password("MyPassword!")
        assert is_valid is False
        assert "digit" in msg

    def test_password_no_special_char(self):
        """Test password without special character"""
        is_valid, msg = validate_password("MyPassword1")
        assert is_valid is False
        assert "special character" in msg

    def test_password_non_string(self):
        """Test password validation with non-string input"""
        is_valid, msg = validate_password(123456789)
        assert is_valid is False


class TestValidateUserData:
    """Test complete user data validation"""

    def test_valid_user_data(self):
        """Test validation of valid user data"""
        data = {
            "name": "John Doe",
            "email": "john@example.com",
            "age": 25,
            "phone": "1234567890",
            "password": "StrongPass1!"
        }
        result = validate_user_data(data)
        assert result["valid"] is True
        assert len(result["errors"]) == 0

    def test_missing_required_fields(self):
        """Test validation with missing required fields"""
        data = {
            "name": "John Doe",
            "email": "john@example.com"
        }
        result = validate_user_data(data)
        assert result["valid"] is False
        assert len(result["errors"]) > 0
        assert any("required" in error.lower() for error in result["errors"])

    def test_invalid_email(self):
        """Test validation with invalid email"""
        data = {
            "name": "John Doe",
            "email": "invalid-email",
            "age": 25,
            "phone": "1234567890",
            "password": "StrongPass1!"
        }
        result = validate_user_data(data)
        assert result["valid"] is False
        assert any("email" in error.lower() for error in result["errors"])

    def test_invalid_age(self):
        """Test validation with invalid age"""
        data = {
            "name": "John Doe",
            "email": "john@example.com",
            "age": 200,
            "phone": "1234567890",
            "password": "StrongPass1!"
        }
        result = validate_user_data(data)
        assert result["valid"] is False
        assert any("age" in error.lower() for error in result["errors"])

    def test_age_under_18_business_rule(self):
        """Test business rule: user must be at least 18"""
        data = {
            "name": "John Doe",
            "email": "john@example.com",
            "age": 16,
            "phone": "1234567890",
            "password": "StrongPass1!"
        }
        result = validate_user_data(data)
        assert result["valid"] is False
        assert any("18" in error for error in result["errors"])

    def test_invalid_phone(self):
        """Test validation with invalid phone"""
        data = {
            "name": "John Doe",
            "email": "john@example.com",
            "age": 25,
            "phone": "123",
            "password": "StrongPass1!"
        }
        result = validate_user_data(data)
        assert result["valid"] is False
        assert any("phone" in error.lower() for error in result["errors"])

    def test_weak_password(self):
        """Test validation with weak password"""
        data = {
            "name": "John Doe",
            "email": "john@example.com",
            "age": 25,
            "phone": "1234567890",
            "password": "weak"
        }
        result = validate_user_data(data)
        assert result["valid"] is False
        assert any("password" in error.lower() for error in result["errors"])

    def test_invalid_name_characters(self):
        """Test validation with invalid characters in name"""
        data = {
            "name": "John123",
            "email": "john@example.com",
            "age": 25,
            "phone": "1234567890",
            "password": "StrongPass1!"
        }
        result = validate_user_data(data)
        assert result["valid"] is False
        assert any("name" in error.lower() for error in result["errors"])

    def test_non_dict_input(self):
        """Test validation with non-dictionary input"""
        result = validate_user_data([1, 2, 3])
        assert result["valid"] is False
        assert any("JSON object" in error for error in result["errors"])

    def test_sanitization_applied(self):
        """Test that sanitization is applied to string fields"""
        data = {
            "name": "  John Doe  ",
            "email": "  john@example.com  ",
            "age": 25,
            "phone": "1234567890",
            "password": "StrongPass1!"
        }
        result = validate_user_data(data)
        assert result["valid"] is True

    def test_name_length_validation(self):
        """Test name length constraints"""
        # Too short
        data = {
            "name": "",
            "email": "john@example.com",
            "age": 25,
            "phone": "1234567890",
            "password": "StrongPass1!"
        }
        result = validate_user_data(data)
        assert result["valid"] is False

        # Too long (101 characters)
        long_name = "A" * 101
        data["name"] = long_name
        result = validate_user_data(data)
        assert result["valid"] is False

    def test_multiple_errors(self):
        """Test that multiple validation errors are reported"""
        data = {
            "name": "123Invalid",
            "email": "invalid-email",
            "age": 200,
            "phone": "123",
            "password": "weak"
        }
        result = validate_user_data(data)
        assert result["valid"] is False
        assert len(result["errors"]) > 2  # Should report multiple errors


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
