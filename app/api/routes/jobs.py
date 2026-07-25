from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.job import Job
from app.schemas.job import JobResponse
from app.schemas.response import SearchResponse
from app.services.job_service import JobService

router = APIRouter()


@router.get("/jobs", response_model=list[JobResponse])
def get_jobs(db: Session = Depends(get_db)):
    jobs = db.query(Job).all()

    return [
        JobResponse(
            id=job.id,
            title=job.title,
            company=job.company,
            location=job.location,
            source=job.source,
            score=job.match_score,
            applied=job.applied,
        )
        for job in jobs
    ]


@router.post("/search", response_model=SearchResponse)
def search_jobs(db: Session = Depends(get_db)):
    service = JobService(db)
    return SearchResponse(**service.search_jobs())