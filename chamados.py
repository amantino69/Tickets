from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # Carrega o arquivo excel em um dataframe
    caminho_arquivo = os.path.join(os.path.expanduser("~"), "Downloads", "Administrar chamados (9).xlsx")
    df = pd.read_excel(caminho_arquivo)
    df['primeiro_nome'] = df['Responsável'].str.split(' ').str[0]

    nomes_manter = ['BRUNO', 'ANA', 'EDGAR', 'MATEUS', 'VICTOR', 'EDER']
    df = df[df['primeiro_nome'].isin(nomes_manter)]
    
    print(df.columns)

    # Converte a coluna "Código" para string e cria a coluna "Código_7"
    df['Código'] = df['Código'].astype(str)
    df['Código_7'] = df['Código'].str[:7]

    # Converte a coluna "Abertura" para datetime
    df['Abertura'] = pd.to_datetime(df['Abertura'])

    # Obtém as datas de início e fim da solicitação
    data_inicial = request.form.get('data_inicial')
    data_final = request.form.get('data_final')

    # Filtra o dataframe com base nas datas de início e fim
    if data_inicial and data_final:
        df = df[(df['Abertura'] >= data_inicial) & (df['Abertura'] <= data_final)]

    # Cria uma tabela dinâmica com 'Status' como colunas
    pivot_table = df.pivot_table(index='primeiro_nome', columns='Status', aggfunc='size', fill_value=0)

    # Adiciona uma coluna de total que soma o conteúdo das linhas
    pivot_table['Total'] = pivot_table.sum(axis=1)

    return render_template('index.html', table=pivot_table.to_html(classes='table table-striped table-bordered'))

if __name__ == '__main__':
    app.run(debug=True)