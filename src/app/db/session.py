from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.app.core.config import Settings

# Step 1. Load Settings
settings = Settings()

# Step 2. Create the SQLAlchemy engine using DB URL from settings in config.py
engine = create_engine(
    settings.database_url,  # This reads your connection string
    echo=False,  # Set to True only for SQL debug logging
    future=True,  # Modern SQLAlchemy, optional but recommended
)

# Step 3. Create a session factory
SessionLocal = sessionmaker(
    autocommit=False,  # You want to commit explicitly for safety
    autoflush=False,  # Prevents automatic DB writes—more control
    bind=engine,
    future=True,  # Consistent with engine
)

# Step 4. Dependency function for FastAPI routes and services


def get_db():
    db: Session = SessionLocal()
    try:
        yield db  # Gives a session to the request handler
    finally:
        db.close()  # Ensures cleanup to avoid memory leaks
