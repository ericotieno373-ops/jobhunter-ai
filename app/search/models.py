from dataclasses import dataclass
from typing import Optional


@dataclass
class JobListing:
    title: str
    company: str
    location: str
    description: str
    url: str

    salary: Optional[str] = None

    source: Optional[str] = None