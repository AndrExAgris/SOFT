# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia o conteúdo do diretório local (no mesmo nível do Dockerfile) para o contêiner
COPY . /app

# Instala as dependências do projeto
RUN pip install --upgrade pip
RUN pip install flask flask_socketio
RUN pip install --no-cache-dir -r requirements.txt
RUN ls

# Expõe a porta que o aplicativo Flask usará
EXPOSE 5000

# Comando para iniciar o aplicativo
CMD ["python", "src/interface/app.py"]
