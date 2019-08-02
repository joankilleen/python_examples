import requests
import commits
import matcher
from test_result import TestResult
from commit import Commit



# Call REST Service and execute test. Extract files from stacktrace.
def execute_test():

	test_url = "http://localhost:8080/async/python"
	headers = {'Accept': 'application/json'}
	test_response = requests.get(test_url, headers=headers)
	if test_response.status_code==200:
		print("Test succeeded")
		return
	print("Test Failed with status: {test_response.status_code}")
	
	stacktrace = test_response.json()['stackTrace']
	stacktrace_files = []
	print(stacktrace)
	for entry in stacktrace:
		if entry.get('fileName'):
			classname = entry["className"]
			filename_and_path = classname.replace(".", "/")
			stacktrace_files.append(filename_and_path)
			print(filename_and_path)
	test_result = TestResult(test_response.status_code, stacktrace_files)
	return test_result

# Main 
repo="AynscWebServiceTester"
git_commits = commits.get_commits_since_date(repo, commit_date="2019-07-31")

# Call a test rest service which generates a NullPointer
test_result = execute_test()
suspect_commits = matcher.match_stacktrace_commits(test_result, git_commits) 



