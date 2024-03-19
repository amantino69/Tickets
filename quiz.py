import pandas as pd

# Carregue os dados da planilha em um DataFrame
df = pd.read_excel('priorizadas_semana.xlsx')

while True:
    # Solicite ao usuário que insira uma pergunta
    pergunta = input("Por favor, insira sua pergunta ou 'sair' para encerrar: ")

    # Se o usuário digitar 'sair', encerre o loop
    if pergunta.lower() == 'sair':
        break

    # Caso contrário, tente responder à pergunta do usuário
    else:
        # Aqui, você pode adicionar o código para responder à pergunta do usuário
        # Por exemplo, se o usuário perguntar "Quantos tickets existem?", você pode fazer:
        if pergunta.lower() == 'quantos tickets existem?':
            print(df['ticket'].count())
        else:
            print("Desculpe, não consigo responder a essa pergunta.")