import pandas as pd
import openai
import config

# Ler dados do CSV usando pandas
data = pd.read_csv('redacoes.csv')

# Configurar a chave da API do OpenAI
openai.api_key = config.OPENAI_API_KEY

# Preparar a conversa de treinamento
conversation = []

# Adicionar exemplos dos dados do CSV como mensagens de treinamento
for _, row in data.iterrows():
    user_message = row['Texto original']
    model_message = row['Reescrita']

    # Adicionar exemplo de entrada e exemplo de saída como se fossem um diálogo
    conversation.append({'role': 'system', 'content': 'Você é um modelo de correção de redações.'})
    conversation.append({'role': 'user', 'content': user_message})
    conversation.append({'role': 'assistant', 'content': model_message})

# Treinar o modelo com a conversa de treinamento
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=conversation
)

# Obter o ID do modelo treinado a partir da resposta
model_id = response['model']['id']

# Salvar o ID do modelo em um arquivo ou variável
with open('model_id.txt', 'w') as file:
    file.write(model_id)




