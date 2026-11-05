from actions.push.commits import notification


def executar(dados):
    repo = dados["repository"]["full_name"]
    autor = dados["sender"]["login"]

    mensagem = f"📦 Repositório **{repo}** foi criado por **{autor}**!"
    notification(mensagem)