from actions.push.commits import notification


def executar(dados):
    repo = dados["repository"]["full_name"]
    autor = dados["pusher"]["name"]
    commit = dados["head_commit"]
    mensagem_commit = commit["message"]
    commit_id = commit["id"][:7]

    mensagem = f"📝 Novo commit em **{repo}** por **{autor}**:\n`{commit_id}` {mensagem_commit}"
    notification(mensagem)
