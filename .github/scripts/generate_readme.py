import os
import requests
import json

def get_pull_request_users(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls"
    response = requests.get(url)
    pull_requests = json.loads(response.text)

    users = set()
    for pr in pull_requests:
        user_login = pr['user']['login']
        users.add(user_login)

    return list(users)

def generate_readme(users, pr_title, pr_description, readme_path):
    with open(readme_path, 'a') as readme:
        readme.write('# Pull Request Contributors\n\n')
        readme.write('List of GitHub users who have submitted pull requests:\n\n')
        for user in users:
            readme.write(f'- {user}\n')

        readme.write('\n\n## Latest Pull Request\n\n')
        readme.write(f'**Title:** {pr_title}\n\n')
        readme.write(f'**Description:** {pr_description}\n\n')

if __name__ == "__main__":
    repo_owner = "gobikaponnusamy"
    repo_name = "hey"

    contributors = get_pull_request_users(repo_owner, repo_name)

    # Get pull request title and description from environment variables
    pr_title = os.getenv('INPUT_PULL_REQUEST_TITLE')
    pr_description = os.getenv('INPUT_PULL_REQUEST_DESCRIPTION')

    # Specify the correct path to README.md
    readme_path = 'README.md'

    generate_readme(contributors, pr_title, pr_description, readme_path)
