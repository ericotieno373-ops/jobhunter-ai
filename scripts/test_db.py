from sqlalchemy import create_engine, text
from app.config.settings import settings

engine = create_engine(settings.DATABASE_URL)

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        print("✅ Connected to PostgreSQL!")
        print(result.scalar())
except Exception as e:
    print("❌ Connection failed")
    print(e)