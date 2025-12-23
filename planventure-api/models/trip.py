from datetime import datetime, timezone
from app import db


class Trip(db.Model):
    """Trip model with user relationship, destination, dates, coordinates, and itinerary."""
    
    __tablename__ = 'trips'
    
    # Primary Key
    id = db.Column(db.Integer, primary_key=True)
    
    # Foreign Key
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    
    # Trip Information
    destination = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    
    # Dates
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    
    # Coordinates (latitude, longitude)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    
    # Itinerary (stored as JSON)
    itinerary = db.Column(db.JSON, default=list)
    
    # Status and metadata
    is_completed = db.Column(db.Boolean, default=False)
    budget = db.Column(db.Float)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    # Relationship to User
    user = db.relationship('User', backref=db.backref('trips', lazy='dynamic', cascade='all, delete-orphan'))
    
    def __repr__(self):
        return f'<Trip {self.destination} ({self.start_date.strftime("%Y-%m-%d")})'
    
    def add_itinerary_item(self, day: int, activity: str, time: str = None, location: str = None, notes: str = None):
        """Add an activity to the trip itinerary."""
        if not isinstance(self.itinerary, list):
            self.itinerary = []
        
        item = {
            'day': day,
            'activity': activity,
            'time': time,
            'location': location,
            'notes': notes
        }
        self.itinerary.append(item)
    
    def get_duration_days(self) -> int:
        """Get the duration of the trip in days."""
        delta = self.end_date - self.start_date
        return delta.days + 1
    
    def to_dict(self) -> dict:
        """Convert trip to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'destination': self.destination,
            'description': self.description,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'duration_days': self.get_duration_days(),
            'latitude': self.latitude,
            'longitude': self.longitude,
            'itinerary': self.itinerary,
            'is_completed': self.is_completed,
            'budget': self.budget,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
