import github_calls

# Find all Joan's repos
url = 'https://api.github.com/users/joankilleen/repos'
response_dict = github_calls.get_from_gitgub(url=url)


repo = response_dict[0]
for repo in response_dict:
	repo_name = repo['name']
	print(f"repo name: {repo_name}")
for repo in response_dict:
	repo_name = repo['name']

	# Get the commits for repo "python_examples"
	if repo_name=='python_examples':
		commits_url = f"https://api.github.com/repos/joankilleen/{repo_name}/commits"
		commits = github_calls.get_from_gitgub(url=commits_url)
		for commit in commits:
			print(f"{commit['sha']}")

