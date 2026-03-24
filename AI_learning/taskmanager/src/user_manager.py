import json
import os
import hashlib
import re
from typing import Optional, Dict
from datetime import datetime

class PasswordStrengthError(Exception):
    pass

class User:
    def __init__(self, username: str, password: str, email: str):
        self.username = username
        self.email = email
        self.created_at = datetime.now().isoformat()
        self.is_verified = False
        self.verification_code = self._generate_verification_code()
        # Hash the password before storing
        self.password_hash = self._hash_password(password)

    def _hash_password(self, password: str) -> str:
        """Hash the password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def _generate_verification_code(self) -> str:
        """Generate a random 6-digit verification code"""
        return ''.join(str(hashlib.sha256(str(datetime.now().timestamp()).encode()).hexdigest())[:6])

    def check_password(self, password: str) -> bool:
        """Verify if the provided password matches the stored hash"""
        return self._hash_password(password) == self.password_hash

    @staticmethod
    def validate_password(password: str) -> bool:
        """
        Validate password strength:
        - At least 8 characters long
        - Contains at least one uppercase letter
        - Contains at least one lowercase letter
        - Contains at least one number
        - Contains at least one special character
        """
        if len(password) < 8:
            raise PasswordStrengthError("Password must be at least 8 characters long")
        if not re.search(r"[A-Z]", password):
            raise PasswordStrengthError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", password):
            raise PasswordStrengthError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", password):
            raise PasswordStrengthError("Password must contain at least one number")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise PasswordStrengthError("Password must contain at least one special character")
        return True

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise ValueError("Invalid email format")
        return True

    def to_dict(self) -> Dict:
        return {
            "username": self.username,
            "email": self.email,
            "password_hash": self.password_hash,
            "created_at": self.created_at,
            "is_verified": self.is_verified,
            "verification_code": self.verification_code
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'User':
        user = cls(data["username"], "", data["email"])  # Empty password as we'll set the hash directly
        user.password_hash = data["password_hash"]
        user.created_at = data["created_at"]
        user.is_verified = data["is_verified"]
        user.verification_code = data["verification_code"]
        return user

class UserManager:
    def __init__(self, file_path: str = "data/users.json"):
        self.file_path = file_path
        self.users: Dict[str, User] = {}
        # Create data directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        self.load_users()

    def load_users(self):
        try:
            with open(self.file_path, 'r') as f:
                users_data = json.load(f)
                self.users = {
                    username: User.from_dict(user_data)
                    for username, user_data in users_data.items()
                }
        except FileNotFoundError:
            self.users = {}
            self.save_users()

    def save_users(self):
        with open(self.file_path, 'w') as f:
            json.dump(
                {username: user.to_dict() for username, user in self.users.items()},
                f,
                indent=4
            )

    def register(self, username: str, password: str, email: str) -> bool:
        """Register a new user. Returns True if successful, False if username already exists."""
        if username in self.users:
            return False
        
        # Validate password strength and email format
        User.validate_password(password)
        User.validate_email(email)
        
        user = User(username, password, email)
        self.users[username] = user
        self.save_users()
        return True

    def login(self, username: str, password: str) -> Optional[User]:
        """Login a user. Returns the User object if successful, None if login fails."""
        user = self.users.get(username)
        if user and user.check_password(password):
            if not user.is_verified:
                raise ValueError("Please verify your email first")
            return user
        return None

    def verify_email(self, username: str, code: str) -> bool:
        """Verify user's email with the provided code"""
        user = self.users.get(username)
        if user and user.verification_code == code:
            user.is_verified = True
            self.save_users()
            return True
        return False

    def user_exists(self, username: str) -> bool:
        """Check if a username already exists"""
        return username in self.users

    def email_exists(self, email: str) -> bool:
        """Check if an email already exists"""
        return any(user.email == email for user in self.users.values()) 