import requests
import commits

def execute_test():

	test_url = "http://localhost:8080/async/python"
	headers = {'Accept': 'application/json'}
	test_response = requests.get(test_url, headers=headers)
	if test_response.status_code==200:
		print("Test succeeded")
		return
	print("Test Failed with status: {test_response.status_code}")
	
	stacktrace = test_response.json()['stackTrace']
	for entry in stacktrace:
		print(entry["className"])
		print(entry['lineNumber'])


repo="AynscWebServiceTester"
response = commits.get_commits_since_date(repo)

# Call a test rest service which generates a NullPointer
execute_test()



