from pydantic import BaseModel


class JobResponse(BaseModel):
    id: int
    title: str
    company: str
    location: str
    source: str
    score: float
    applied: bool

    model_config = {
        "from_attributes": True
    }