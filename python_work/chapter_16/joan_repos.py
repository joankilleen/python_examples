import requests

   # Make an API call and store the response.
url = 'https://api.github.com/users/joankilleen/repos'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)

# Store API response in a variable.
response_dict = r.json()

# Process results.
repo = response_dict[0]
for repo in response_dict:
	repo_name = repo['name']
	print(f"repo name: {repo_name}")
for repo in response_dict:
	repo_name = repo['name']
	if repo_name=='python_examples':
		commits_url = f"https://api.github.com/repos/joankilleen/{repo_name}/commits"
		r_commits = requests.get(commits_url, headers=headers)
		print(f"Commits Status code: {r_commits.status_code}")
		commits = r_commits.json()
		for commit in commits:
			print(f"{commit['sha']}")
		
#  	
# 	
#           
#          
#           print(f"Commits Status code: {r_commits.status_code}")
#           
     
# # repo_name = repo['name']

# # commits_url = f"https://api.github.com/repos/joankilleen/{repo_name}/commits"

# # r_commits = requests.get(commits_url, headers=headers)
# # print(f"Commits Status code: {r.status_code}")
# # print(f"{r_commits.json()}")
