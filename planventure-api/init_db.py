"""
Database initialization script.
Run this script to create all database tables.

Usage:
    python init_db.py
"""

import os
from app import app, db


def init_database():
    """Initialize the database by creating all tables."""
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        print("✓ Database tables created successfully!")
        print(f"Database location: {os.getenv('DATABASE_URL', 'sqlite:///planventure.db')}")


if __name__ == '__main__':
    init_database()
