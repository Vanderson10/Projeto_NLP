from flask import Flask, request, jsonify
import openai
import config

# Configure a chave da API do OpenAI
openai.api_key = config.OPENAI_API_KEY

app = Flask(__name__)

# Função para criar uma conversa interativa
def criar_conversa(redacao, modelo):
    conversa = [
        {"role": "system", "content": "Você é um assistente de linguagem que irá corrigir a redação."},
        {"role": "user", "content": redacao}
    ]

    response = openai.ChatCompletion.create(
        model=modelo,  # Use o modelo desejado, por exemplo, "gpt-3.5-turbo"
        messages=conversa
    )

    return response['choices'][0]['message']['content']

# @app.route('/corrigir_redacao', methods=['POST'])
def corrigir_redacao_endpoint(redacao):
    # dados = request.get_json()
    # redacao = dados.get('redacao')

    if redacao:
        modelo = 'gpt-3.5-turbo'  # Substitua pelo modelo desejado
        correcao = criar_conversa(redacao, modelo)
        # return jsonify({"correcao": correcao})
    # else:
        # return jsonify({"erro": "Redação não fornecida"})

# if __name__ == "__main":
#     app.run()

print(corrigir_redacao_endpoint("A imposição de padrões culturais e a obsessão por verdades absolutas impedem religiosos conservadores de conviver com as diferenças, o que acaba gerando a intolerância religiosa. Isso ocorre devido à falta do sentimento de coexistência, por parte dos intolerantes, com a fé do outro. Esse problema está enraizado na nossa história, um exemplo disso são os constantes ataques às religiões afro-brasileiras, nos quais os próprios agressores julgam a fé alheia sem mesmo conhecê-la ou até mesmo na imposição da religião cristã aos antigos nativos que aqui habitavam. Segundo Edgar Morin, mudanças de pensamento implicam, antes de tudo, em mudanças na educação, ou seja, teremos que mudar a nossa educação de individual e tecnicista, para uma mais humana e coletiva. Além disso, para revertermos esse quadro, a laicidade do Estado deveria ser assegurada e políticas de opressão a esse tipo de agressão deveriam ser tomadas, como por exemplo, o aumento da pena para quem cometer esses crimes e uma maior campanha de denúncia. A fim de assegurar o avanço contra essas práticas, uma medida à médio-longo prazo, seria a implementação da disciplina Ensino religioso nas escolas brasileiras. Essa disciplina, testada em escolas suecas, consiste em mostrar de maneira imparcial religiões de todos os continentes para que a visão de mundo do aluno seja ampliada desde sua infância, o que pode ajudar, de maneira direta, à redução desse problema"))