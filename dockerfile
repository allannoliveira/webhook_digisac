FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /app

# Copia arquivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Porta
EXPOSE 8080

# Rodar com gunicorn (produção)
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]