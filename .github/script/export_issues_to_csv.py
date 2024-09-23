import csv
import os
from github import Github

# Set up GitHub access token
token = os.getenv('GITHUB_TOKEN')  # Using GITHUB_TOKEN provided by GitHub Actions
repo_name = os.getenv('GITHUB_REPOSITORY')

# Initialize GitHub API client
g = Github(token)
repo = g.get_repo(repo_name)

# Fetch issues from the repository
issues = repo.get_issues(state='all')

# Create CSV file
csv_file = '.github/issues.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Issue Number', 'Title', 'State', 'Created At', 'Updated At', 'URL'])

    for issue in issues:
        writer.writerow([issue.number, issue.title, issue.state, issue.created_at, issue.updated_at, issue.html_url])

print(f"Exported {issues.totalCount} issues to {csv_file}")
