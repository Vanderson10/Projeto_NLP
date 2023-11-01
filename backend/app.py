from flask import Flask, request, jsonify
from prompt import prompt
import openai
import config
from flask_cors import CORS


openai.api_key = config.OPENAI_API_KEY

app = Flask(__name__)
CORS(app)


@app.route('/corrigir_redacao', methods=['POST'])
def get_completion(model="gpt-3.5-turbo"):

    data = request.get_json()

    redacao = data['redacao']

    messages = [
        {"role": "system", "content": prompt()},
        {"role": "user", "content": redacao},
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return jsonify({"correcao": response.choices[0].message["content"]})


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
