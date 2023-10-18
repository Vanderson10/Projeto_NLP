from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

with open('model_id.txt', 'r') as file:
    model_id = file.read().strip()

@app.route('/corrigir_redacao', methods=['POST'])
def corrigir_redacao():
    data = request.get_json()
    redacao = data['redacao']

    system_message = "Você é um modelo que corrige redações com base no livro Produção textual na linha da argumentação."

    # Adicionar mensagem do usuário com base no texto a ser corrigido
    user_message = redacao

    # Utilize o ID do modelo treinado
    conversation = [
        system_message,
        user_message,
    ]

    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )

    correcao = response.choices[0].message['content']

    return jsonify({'correcao': correcao})

