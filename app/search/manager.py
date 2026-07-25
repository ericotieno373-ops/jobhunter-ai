from app.search.providers.corporate_staffing import CorporateStaffingProvider
from app.search.providers.myjobmag import MyJobMagProvider
from app.utils.logger import logger


class SearchManager:

    def __init__(self):
        self.providers = [
            CorporateStaffingProvider(),
            MyJobMagProvider(),
        ]

    def search(self):

        jobs = []

        for provider in self.providers:

            logger.info(
                "Searching provider: %s",
                provider.__class__.__name__,
            )

            try:
                jobs.extend(provider.search())

            except Exception:
                logger.exception(
                    "Provider failed: %s",
                    provider.__class__.__name__,
                )

        logger.info("Total jobs found: %s", len(jobs))

        return jobs