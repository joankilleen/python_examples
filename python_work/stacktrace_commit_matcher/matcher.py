from test_result import TestResult
from commit import Commit

def match_stacktrace_commits(test_result, commits):
	suspect_commits = []
	if test_result.status_code == 200:
		return suspect_commits

	for commit in commits:
		for filename in commit.filenames:
			for filename_and_path in test_result.filenames_and_paths:
				# print(f"Next filename in commit {filename}")
				# print(f"filename_and_path {filename_and_path}")
				# print()
				if (filename.find(filename_and_path) != -1):
					print(f"Matched file: {filename}")
					suspect_commits.append(commit) 
					break
	print("Suspect commits")
	for object in suspect_commits:
		print(f"Sha: {object.sha}")

	return suspect_commits