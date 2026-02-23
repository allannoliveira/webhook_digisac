🚀 Webhook Digisac → Google Chat
Este projeto cria uma integração entre o Digisac e o Google Chat, enviando uma notificação visual (Card) sempre que um novo atendimento é iniciado.

🎯 Objetivo
Notificar automaticamente no Google Chat quando:

Um cliente iniciar uma conversa no Digisac
O bot enviar a primeira mensagem automática
A conexão for específica (ex: HELP DESK)
🧠 Como Funciona
Fluxo da integração:

Cliente envia mensagem
↓
Digisac cria ticket
↓
Bot responde automaticamente
↓
Webhook recebe message.created
↓
Sistema envia Card visual para Google Chat

🔧 Tecnologias Utilizadas
Python 3.x
Flask
Requests
Ngrok (para ambiente local)
Google Chat Webhook
📦 Instalação
1️⃣ Clone o projeto
git clone https://seu-repositorio.git
cd webhook-digisac
2️⃣ Instale as dependências
pip install flask requests
⚙️ Configuração

No arquivo main.py, configure:

SERVICE_ID_PERMITIDO = "SEU_SERVICE_ID"
GOOGLE_CHAT_WEBHOOK = "SUA_URL_DO_GOOGLE_CHAT"
▶️ Executando o Projeto
python main.py

Deve aparecer:

Running on http://127.0.0.1:5000
🌍 Expondo Localmente com Ngrok
ngrok http 5000

Use a URL gerada no Digisac:

https://xxxx.ngrok-free.app/webhook/digisac
📡 Evento Monitorado

O sistema escuta:

event: message.created

E valida:

serviceId igual ao configurado

isFromBot == True

🖥️ Resultado no Google Chat

Envia um Card visual contendo:

🚨 Novo Atendimento

Informação de que um cliente iniciou conversa

Botão para acessar o Digisac

🔐 Segurança (Opcional)

Você pode adicionar validação por token:

if request.headers.get("X-Token") != "SEU_TOKEN":
    return jsonify({"erro": "não autorizado"}), 403
📈 Melhorias Futuras

Persistência de tickets notificados (MySQL)

Suporte multi-conexão

Logs estruturados

Deploy em produção (Render / VPS)

Monitoramento de SLA

Dashboard interno

🏢 Estrutura do Projeto
webhook-digisac/
│
├── main.py
├── requirements.txt
└── README.md
👨‍💻 Autor

Desenvolvido por Allan Oliveira
Analista de T.I | Backend Python | Automação e Integrações
