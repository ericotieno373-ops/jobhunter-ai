from sqlalchemy.orm import Session

from app.models.job import Job
from app.search.models import JobListing


class JobRepository:

    def __init__(self, db: Session):
        self.db = db

    def exists(self, url: str) -> bool:

        return (
            self.db.query(Job)
            .filter(Job.url == url)
            .first()
            is not None
        )

    def create(self, job: JobListing):

        if self.exists(job.url):
            return False

        db_job = Job(
            title=job.title,
            company=job.company,
            location=job.location,
            description=job.description,
            salary=job.salary,
            url=job.url,
            source=job.source,
        )

        self.db.add(db_job)
        self.db.commit()

        return True