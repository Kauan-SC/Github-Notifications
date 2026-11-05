from actions.push.commits import notification


def executar(dados):
    repo = dados["repository"]["full_name"]
    ref = dados["ref"]
    autor = dados["pusher"]["name"]

    mensagem = f"🌱 Nova branch **{ref}** criada em **{repo}** por **{autor}**!"
    notification(mensagem)