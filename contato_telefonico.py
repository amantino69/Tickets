from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import os
import re
import nltk
from nltk.corpus import names

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # Carrega o arquivo excel em um dataframe
    caminho_arquivo = os.path.join(os.path.expanduser("~"), "Downloads", "Administrar chamados (12).xlsx")
    df = pd.read_excel(caminho_arquivo)
    
    # Mater apenas as colunas código, flex9 e flex11
    df = df[['Código', 'Contato', 'Telefone1', 'Telefone2']]

    # Exclua valores não numéricos da coluna telefone1
    df['Telefone1'] = df['Telefone1'].astype(str).str.replace(r'\D+', '')
    
    df['Telefone1'] = df['Telefone1'].replace('[^0-9]', '', regex=True)
    df['Telefone2'] = df['Telefone2'].replace('[^0-9]', '', regex=True)

    # Exclua NaN de todas a linhas das colunas Telefone1 e Telefone2 substituindo por espaço em branco
    df['Telefone1'] = df['Telefone1'].fillna('')
    df['Telefone2'] = df['Telefone2'].fillna('')
    df['Contato'] = df['Contato'].fillna('')
    
    # Para as linha não vazias, aplicar Máscara de data no formato (99)9999-9999 nos números de telefone1 e telefone2
    df['Telefone1'] = df['Telefone1'].apply(lambda x: '({}){}-{}'.format(x[:2], x[2:6], x[6:]) if x else '')
    df['Telefone2'] = df['Telefone2'].apply(lambda x: '({}){}-{}'.format(x[:2], x[2:6], x[6:]) if x else '')
    
    # Exclua linhas quando não existir Telefone1 e Telefone2 simultaneamente. Se um dos telefone forem diferente de vazio não exclua a linha
    df = df[(df['Telefone1'] != '') | (df['Telefone2'] != '')]

    # Percorra todas linhas df e quando Telefone2 for vazio, copie o valor de Telefone1 para Telefone2
    df['Telefone2'] = df.apply(lambda x: x['Telefone1'] if x['Telefone2'] == '' else x['Telefone2'], axis=1)
     
    # Baixe a lista de nomes se ainda não tiver feito isso
    nltk.download('names')

    # Crie um conjunto de todos os nomes para pesquisa rápida
    all_names = set(names.words())

    # Defina uma função para remover palavras que não são nomes
    def remove_non_names(s):
        return ' '.join(word for word in s.split() if word in all_names)

    # Aplique a função à coluna "Contato"
    df['Contato'] = df['Contato'].apply(remove_non_names)
        # Utilizando uma biblioteca human-names, crie uma coluna com o primeiro nome do Contato
            
    # Eliminar repetições considerando as colunas Contato e Telefone2
    df = df.drop_duplicates(subset=['Contato', 'Telefone2'])
        

    
    
    return render_template('index_contato_telefonico.html', table=df.to_html(classes='table table-striped'))


if __name__ == '__main__':
    app.run(debug=True)    