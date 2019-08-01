import requests

def get_from_gitgub(url):
	headers = {'Accept': 'application/vnd.github.v3+json'}
	r = requests.get(url, headers=headers)
	print(f"Status Code {r.status_code} for url: {url}")
	return r