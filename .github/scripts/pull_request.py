from github import Github
import os

# Autenticação via token de acesso pessoal
token = os.getenv("GITHUB_TOKEN")  # Pode ser passado como variável de ambiente no GitHub Actions
branch = os.getenv("GITHUB_BRANCH")

g = Github(token)

# Informações necessárias
repo_name = os.getenv("GITHUB_REPO")  # Nome do repositório
source_branch = branch
target_branch = "main"
titulo_pr = branch
descricao_pr = "PR criada automaticamente."

# Conectar ao repositório
repo = g.get_repo(repo_name)

# Criar a pull request
pr = repo.create_pull(
    title=titulo_pr,
    body=descricao_pr,
    head=source_branch,
    base=target_branch
)

print(f"Pull Request criada: {pr.html_url}")
