from github import Github
import os

def create_github_issue(repo_name, issue_title, issue_body, token):
    # Autenticação com o token do GitHub
    g = Github(token)

    # Acessar o repositório
    repo = g.get_repo(repo_name)

    # Criar uma nova issue
    issue = repo.create_issue(
        title=issue_title,
        body=issue_body
    )

    print(f"Issue criada com sucesso: {issue.html_url}")

if __name__ == "__main__":
    # Variáveis de ambiente
    repo_name = os.getenv('GITHUB_REPOSITORY')
    issue_title = os.getenv('ISSUE_TITLE', 'Automated Issue Title')
    issue_body = os.getenv('ISSUE_BODY', 'This issue was created automatically by GitHub Actions.')
    github_token = os.getenv('GITHUB_TOKEN')

    create_github_issue(repo_name, issue_title, issue_body, github_token)
