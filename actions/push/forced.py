from actions.push.commits import notification


def executar(dados):
    repo = dados["repository"]["full_name"]
    ref = dados["ref"]
    autor = dados["pusher"]["name"]

    mensagem = f"⚠️ Push forçado (force-push) em **{ref}** de **{repo}** por **{autor}**!"
    notification(mensagem)