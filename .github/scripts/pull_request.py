from github import Github

# Autenticação via token de acesso pessoal
token = "GITHUB_TOKEN"  # Pode ser passado como variável de ambiente no GitHub Actions
g = Github(token)

# Informações necessárias
repo_name = "owner/repo_name"  # Nome do repositório
source_branch = "branch-de-alteracoes"
target_branch = "main"
titulo_pr = "Minha nova Pull Request"
descricao_pr = "Essa PR contém as alterações XYZ."

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
