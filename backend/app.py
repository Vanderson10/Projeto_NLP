from flask import Flask, request, jsonify
from prompt import prompt
import openai
import config
from flask_cors import CORS


openai.api_key = config.OPENAI_API_KEY

app = Flask(__name__)
CORS(app)

# texto = f"""
# ‘’’Tema: VALORIZAÇÃO DO IDOSO

# É inegável que a evolução da ciência e da tecnologia contribuiu para a criação de novas formas de combate à mortalidade e provocou um aumento significativo da expectativa de vida. Porém a imposição de padrões rígidos de classificação do “velho” e do “novo”, as relações de poder impressas pela sociedade de consumo e um sistema educacional desvinculado das questões essenciais da formação humana levam, respectivamente, à incompreensão do envelhecimento natural e à coi-
# sificação e descarte dos idosos.
# Segundo pesquisa realizada pela Sociedade Internacional de Cirurgias Plásticas Estéticas, mostra-se crescente o número de indivíduos, em todo o mundo, que, insatisfeitos com a aparência não-juvenil, procuram clínicas de estética para reverterem tal situação. No Brasil, o número supera um milhão de casos, o que consome a 13 % do total mundial. Essa procura parece se dá pelo fato de muitos não terem sido educados, desde a infância, de forma a compreenderem o processo natural de envelhecimento e, consequentemente, não desenvolverem o respeito às diferenças atuais e futuras, o que causa aversão a qualquer desvio dos padrões impostos.
# É importante destacar, também, que a sociedade de consumo mostra como principal criadora de estereótipos, nos quais a jovialidade está ligada ao consumo modern. Nesse papel de estereotipação, utiliza-se o poderoso instrumento para se instaurar modelos de beleza, que estão relacionados, de forma quase total, a jovens em propagandas de produtos cada vez mais novos. Reforça-se, assim, a ideologia de que o novo é o bom; já o velho deve ser descartado. Diante disso, há, cada vez mais, um distanciamento nas relações interpessoais entre idosos e jovens, pois estes vêem aqueles como símbolo do retrocesso, objetos descartados.
# Dessa maneira, fica perceptível que o respeito ao idoso está longe do que deveria ser, pois ainda é preciso quebrar paradigmas e imposições que levam ao subjugamento de pessoas. Nessa perspectiva, é preciso que ONG´s, juntamente, com a mídia, realizem campanhas que valorizem o idoso, apontando qualidades como a experiência e a contribuição dada para a estruturação da sociedade. Ainda, a escola e a família devem preparar crianças para terem respeito às diferenças e para se conscientizarem do processo biológico do envelhecimento, através de visitas periódicas a casas
# de acolhimento de idosos. Cabe ainda à família planejar o conforto e a ambientação do idoso por meio de adaptações em imóveis, móveis e transportes.’’’

# """

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
        temperature=0, # this is the degree of randomness of the model's output
    )
    return jsonify({"correcao": response.choices[0].message["content"]})

# response = get_completion(prompt())
# print(response)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)