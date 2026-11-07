import hashlib
import hmac
import os

from dotenv import load_dotenv

load_dotenv()

# Webhooks:
github = os.environ["GITHUB_WEBHOOK_SECRET"]


def verificar_assinatura(request) -> bool:
    assinatura_recebida = request.headers.get("X-Hub-Signature-256")
    if not assinatura_recebida:
        return False

    hash_esperado = hmac.new(
        github.encode("utf-8"),
        msg=request.data,
        digestmod=hashlib.sha256,
    ).hexdigest()
    assinatura_esperada = f"sha256={hash_esperado}"

    return hmac.compare_digest(assinatura_esperada, assinatura_recebida)