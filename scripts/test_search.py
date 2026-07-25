from app.search.manager import SearchManager

jobs = SearchManager().search()

print(f"\nFound {len(jobs)} jobs\n")

for job in jobs[:10]:
    print("=" * 60)
    print(job.title)
    print(job.url)