import re

def validate_email(email):
    """Simple email validation"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Simple phone validation - accepts +country code and digits"""
    pattern = r'^\+?[1-9]\d{1,14}$'
    return re.match(pattern, phone) is not None

def validate_emails(emails):
    """Validate list of emails"""
    if not isinstance(emails, list) or len(emails) == 0:
        return False, "Emails list cannot be empty"
    
    for email in emails:
        if not validate_email(email):
            return False, f"Invalid email: {email}"
    return True, "Valid"

def validate_phones(phones):
    """Validate list of phones"""
    if not isinstance(phones, list) or len(phones) == 0:
        return False, "Phones list cannot be empty"
    
    for phone in phones:
        if not validate_phone(phone):
            return False, f"Invalid phone: {phone}"
    return True, "Valid"
