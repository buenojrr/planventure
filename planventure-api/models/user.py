from datetime import datetime, timezone 
from app import db
from bcrypt import hashpw, gensalt, checkpw


class User(db.Model):
    """User model with email, password_hash, and timestamps."""
    
    __tablename__ = 'users'
    
    # Primary Key
    id = db.Column(db.Integer, primary_key=True)
    
    # User Information
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    
    # User Details
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f'<User {self.email}>'
    
    def set_password(self, password: str) -> None:
        """Hash and set the user's password."""
        self.password_hash = hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')
    
    def check_password(self, password: str) -> bool:
        """Verify the user's password."""
        return checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))
    
    def to_dict(self) -> dict:
        """Convert user to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
