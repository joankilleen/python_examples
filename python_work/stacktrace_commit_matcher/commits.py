from commit import Commit
from datetime import date
import github_calls

def get_commits_since_date(repo, commit_date):
   commits_url = f"https://api.github.com/repos/joankilleen/{repo}/commits?since={commit_date}"
   print(commits_url)

   # Git all commits for date from Github
   response = github_calls.get_from_gitgub(url=commits_url)

   if response.status_code != 200:
   	raise Exception(f"Commits could not be read from GitHub {response.status_code}")

   json = response.json()
   commits = []

   # Iterate over commit
   for json_object in json:
   	sha = json_object['sha']
   	commit_detail_url = f"https://api.github.com/repos/joankilleen/{repo}/commits/{sha}"

   	# Get details of commit from GitHub
   	reponse_for_commit = github_calls.get_from_gitgub(url=commit_detail_url)
   	print(f"{reponse_for_commit.status_code}")

   	if reponse_for_commit.status_code != 200:
   		raise Exception(f"Commit {sha} could not be read from GitHub {reponse_for_commit.status_code}")  

   	# Read the changed files in the commit
   	files = reponse_for_commit.json()['files']

   	filenames = []
   	for file in files:
   		print(file['filename'])
   		filenames.append(file['filename'])
   	# Create a Commit object
   	commit = Commit(sha, filenames)
   	print(commit.sha)
   	commits.append(commit)
   
   print(len(commits))
   return commits


