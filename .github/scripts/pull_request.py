from github import Github
import os

# Autenticação via token de acesso pessoal
token = os.getenv("GITHUB_TOKEN")  # Pode ser passado como variável de ambiente no GitHub Actions
g = Github(token)

# Informações necessárias
repo_name = "rtechthiago0/auto_pr"  # Nome do repositório
source_branch = "CGH-112233"
target_branch = "main"
titulo_pr = "CGH-112233"
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
