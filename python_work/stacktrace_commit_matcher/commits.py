from commit import Commit
from datetime import date
import github_calls

def get_commits_for_date(repo, commit_date=date.today()):
   print(f"{commit_date.strftime('%Y-%m-%d')}")
   commits_url = f"https://api.github.com/repos/joankilleen/{repo}/commits?commiter-date={commit_date}"
   print(commits_url)
   github_calls.get_from_gitgub(url=commits_url)