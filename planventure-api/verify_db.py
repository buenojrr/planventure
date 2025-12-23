"""
Verify database tables were created.
"""

from app import app, db
from sqlalchemy import inspect


def verify_tables():
    """Check which tables were created in the database."""
    with app.app_context():
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        
        print("✓ Database tables created:")
        for table in tables:
            columns = inspector.get_columns(table)
            print(f"\n  {table}:")
            for col in columns:
                print(f"    - {col['name']} ({col['type']})")


if __name__ == '__main__':
    verify_tables()
