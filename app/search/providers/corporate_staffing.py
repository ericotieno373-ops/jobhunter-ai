from app.search.base import BaseProvider
from app.search.models import JobListing
from app.services.scraper import WebScraper


class CorporateStaffingProvider(BaseProvider):

    URL = "https://www.corporatestaffing.co.ke/jobs/"

    def search(self):

        soup = WebScraper.get(self.URL)

        jobs = []

        # Find every "View Job Details" link
        links = soup.find_all("a", string=lambda s: s and "View Job Details" in s)

        for link in links:

            href = link.get("href")

            if not href:
                continue

            # Find the nearest heading before the link
            title_tag = link.find_previous(["h2", "h3"])

            title = title_tag.get_text(strip=True) if title_tag else "Unknown Job"

            jobs.append(
                JobListing(
                    title=title,
                    company="Unknown",
                    location="Kenya",
                    description="",
                    url=href,
                    source="Corporate Staffing",
                )
            )

        return jobs