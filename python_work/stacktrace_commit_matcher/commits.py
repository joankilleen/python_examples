from commit import Commit
from datetime import date
import github_calls

def get_commits_since_date(repo, commit_date=date.fromordinal(date.today().toordinal()-1)):
   print(f"{commit_date.strftime('%Y-%m-%d')}")
   commits_url = f"https://api.github.com/repos/joankilleen/{repo}/commits?since={commit_date}"
   print(commits_url)
   response = github_calls.get_from_gitgub(url=commits_url)

   if response.status_code != 200:
   	raise Exception(f"Commits could not be read from GitHub {response.status_code}")

   json = response.json()
   for json_object in json:
   	print(f"{json_object['sha']}")