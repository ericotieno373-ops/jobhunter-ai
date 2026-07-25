from sqlalchemy.orm import Session

from app.repositories.job_repository import JobRepository
from app.search.manager import SearchManager


class JobService:

    def __init__(self, db: Session):
        self.db = db
        self.repo = JobRepository(db)

    def search_jobs(self):

        jobs = SearchManager().search()

        saved = 0

        for job in jobs:

            if self.repo.create(job):
                saved += 1

        return {
            "found": len(jobs),
            "saved": saved
        }