from app.database.session import SessionLocal
from app.repositories.job_repository import JobRepository
from app.search.manager import SearchManager

db = SessionLocal()

repo = JobRepository(db)

jobs = SearchManager().search()

saved = 0

for job in jobs:

    if repo.create(job):
        saved += 1

print(f"Saved {saved} new jobs.")