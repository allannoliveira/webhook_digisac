from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GOOGLE_CHAT_WEBHOOK = "https://chat.googleapis.com/v1/spaces/AAQAaEaO3xU/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=N7jM9c673N5AaThrs3XLUaRxH3iaoYnzD7Kok9dv-dI"
SERVICE_ID_PERMITIDO = "0224d753-98a1-481a-968e-0cee6337c4f5"

@app.route("/webhook/digisac", methods=["POST"])
def webhook_digisac():
    payload = request.json

    if payload.get("event") != "message.created":
        return jsonify({"status": "evento ignorado"}), 200

    mensagem_data = payload.get("data", {})

    if mensagem_data.get("serviceId") != SERVICE_ID_PERMITIDO:
        return jsonify({"status": "conexao ignorada"}), 200

    if mensagem_data.get("isFromBot") is not True:
        return jsonify({"status": "não é bot"}), 200

    # 🔥 Card visual
    card_payload = {
        "cardsV2": [
            {
                "cardId": "novo_atendimento",
                "card": {
                    "header": {
                        "title": "🚨 Novo Atendimento",
                        "subtitle": "Digisac - HELP DESK"
                    },
                    "sections": [
                        {
                            "widgets": [
                                {
                                    "textParagraph": {
                                        "text": "<b>Uma pessoa iniciou uma conversa.</b>"
                                    }
                                },
                                {
                                    "buttonList": {
                                        "buttons": [
                                            {
                                                "text": "Acessar Digisac",
                                                "onClick": {
                                                    "openLink": {
                                                        "url": "https://app.digisac.co"
                                                    }
                                                }
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }

    requests.post(GOOGLE_CHAT_WEBHOOK, json=card_payload)

    return jsonify({"status": "notificado"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)