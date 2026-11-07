import requests

from constants import Bot_webhook


def notification(mensagem):

    dados = {
        **mensagem,
        "username": "Matte Infos",
    }

    resposta = requests.post(Bot_webhook, json=dados)

    if resposta.status_code == 204:
        print("Notificação enviada com sucesso!")
    else:
        print(f"Erro ao enviar: {resposta.status_code}")