from pydantic import BaseModel


class SearchResponse(BaseModel):
    found: int
    saved: int