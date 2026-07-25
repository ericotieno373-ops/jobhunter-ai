from app.database.base import Base
from app.database.connection import engine

# Import models
from app.models.job import Job

Base.metadata.create_all(bind=engine)

print("✅ Database initialized successfully.")