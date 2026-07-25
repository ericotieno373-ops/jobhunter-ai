from abc import ABC
from abc import abstractmethod

from app.search.models import JobListing


class BaseProvider(ABC):

    @abstractmethod
    def search(self) -> list[JobListing]:
        """
        Return a list of jobs.
        """
        pass