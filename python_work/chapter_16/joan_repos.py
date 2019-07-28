import requests

   # Make an API call and store the response.
url = 'https://api.github.com/users/joankilleen/repos'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)

# Store API response in a variable.
response_dict = r.json()

# Process results.
repo = response_dict[0]
# for key in sorted(repo.keys()):
#     print(key)
# print(f"repo name: {repo['name']}")

repo_name = repo['name']

commits_url = f"https://api.github.com/repos/joankilleen/{repo_name}/commits"

r_commits = requests.get(commits_url, headers=headers)
print(f"Commits Status code: {r.status_code}")
print(f"{r_commits.json()}")
