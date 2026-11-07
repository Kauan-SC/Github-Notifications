from flask import Flask, request

from actions.push import created as push_created
from actions.push import deleted as push_deleted
from actions.push import forced, head_commit
from actions.repository import created as repo_created
from actions.repository import deleted as repo_deleted
from actions.repository import edited, renamed
from verification import verificar_assinatura

app = Flask(__name__)

@app.route("/webhookcallback", methods=["POST"])
def hook():
    if not verificar_assinatura(request):
        return "Assinatura invalida", 403

    evento = request.headers.get("X-GitHub-Event")
    dados = request.json

# ------------------------------------------------------------------------------

    # Se evento for um repositório
    if evento == "repository":
        acao = dados.get("action")

        # Repositório criado
        if acao == "created":
            repo_created.executar(dados)

        # Repositório deletado
        if acao == "deleted":
            repo_deleted.executar(dados)

        # Repositório renomeado   
        if acao == "renamed":
            renamed.executar(dados)

        # Repositório editado
        if acao == "edited":
            edited.executar(dados)

# ------------------------------------------------------------------------------

    #  Se evento for um Push
    if evento == "push":
        
        # Dados criados
        if dados.get("created"):
            push_created.executar(dados)

        # Dados deletados
        if dados.get("deleted"):
            push_deleted.executar(dados)

        # Dados forçados
        if dados.get("forced"):
            forced.executar(dados)
        
        # Dados do commit
        if dados.get("head_commit"):
            head_commit.executar(dados)



    print(request.data)
    return "OK", 200

if __name__ == "__main__":
    app.run()

