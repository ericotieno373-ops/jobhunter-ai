from app.services.scraper import WebScraper

url = "https://www.corporatestaffing.co.ke/jobs/"

soup = WebScraper.get(url)

print(soup.title.text)