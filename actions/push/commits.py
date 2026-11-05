import requests

from constants import Bot_webhook


def notification(mensagem):

    dados = {
        "content": mensagem,
        "username": "Matte Infos",
    }

    resposta = requests.post(Bot_webhook, json=dados)

    if resposta.status_code == 204:
        print("Notificação enviada com sucesso!")
    else:
        print(f"Erro ao enviar: {resposta.status_code}")


def executar(dados):
    repo = dados["repository"]["full_name"]
    autor = dados["pusher"]["name"]
    commit = dados["head_commit"]
    mensagem_commit = commit["message"]
    commit_id = commit["id"][:7]

    mensagem = f"📝 Novo commit em **{repo}** por **{autor}**:\n`{commit_id}` {mensagem_commit}"
    notification(mensagem)