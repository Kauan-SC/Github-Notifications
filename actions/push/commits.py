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

    message_data = {
    "flags": 32768,
    "components": [
        {
        "type": 17,
        "components": [
            {
            "type": 10,
            "content": f"📝 Novo commit em **{repo}** por **{autor}**."
            },
            {
            "type": 14,
            "spacing": 1,
            "divider": True
            },
            {
            "type": 10,
            "content": f"ID do commit: {commit_id}"
            },
            {
            "type": 14,
            "spacing": 1,
            "divider": True
            },
            {
            "type": 10,
            "content": f"Mensagem de Commit: {mensagem_commit}"
            }
        ]
        }
    ]
    }


    notification(message_data)