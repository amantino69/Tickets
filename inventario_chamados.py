from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import os

app = Flask(__name__)



@app.route('/totals', methods=['GET', 'POST'])
def totals():
    # Carrega o arquivo excel em um dataframe
    caminho_arquivo = os.path.join(os.path.expanduser("~"), "Downloads", "ReportBook.xlsx")
    df = pd.read_excel(caminho_arquivo)

    # Converte a coluna "Código" para string e cria a coluna "Código_8"
    df['Código'] = df['Código'].astype(str)
    df['Código_8'] = df['Código'].str[:8]

    # Cria uma tabela dinâmica com 'Status' como colunas
    pivot_table = df.pivot_table(index='Código_8', columns='Status', aggfunc='size', fill_value=0)

    # Calcula o número de linhas após o agrupamento
    num_linhas = pivot_table.shape[0]

    # Calcula os totais de linhas e colunas
    total_linhas = df.shape[0]
    total_colunas = df.shape[1]

    return render_template('totals.html', total_linhas=total_linhas, total_colunas=total_colunas, num_linhas=num_linhas)
@app.route('/', methods=['GET', 'POST'])
def home():
    # Carrega o arquivo excel em um dataframe
    caminho_arquivo = os.path.join(os.path.expanduser("~"), "Downloads", "ReportBook.xlsx")
    df = pd.read_excel(caminho_arquivo)
    df['Nome'] = df['Responsável'].str.split(' ').str[0]

    # nomes_manter = ['BRUNO', 'ANA', 'EDGAR', 'MATEUS', 'VICTOR', 'EDER']
    # df = df[df['primeiro_nome'].isin(nomes_manter)]
    
    print(df.columns)    
    

    # Converte a coluna "Código" para string e cria a coluna "Código_7"
    df['Código'] = df['Código'].astype(str)
    df['Código_8'] = df['Código'].str[:8]

    # Converte a coluna "Abertura" para datetime
    df['Abertura'] = pd.to_datetime(df['Abertura'])

    # Obtém as datas de início e fim da solicitação
    data_inicial = request.form.get('data_inicial')
    data_final = request.form.get('data_final')

    # Filtra o dataframe com base nas datas de início e fim
    if data_inicial and data_final:
        df = df[(df['Abertura'] >= data_inicial) & (df['Abertura'] <= data_final)]

    # Cria uma tabela dinâmica com 'Status' como colunas
    # pivot_table = df.pivot_table(index='Código', columns='Status', aggfunc='size', fill_value=0)
    pivot_table = df.pivot_table(index='Código_8', columns='Status', aggfunc='size', fill_value=0)

    # Adiciona uma coluna de total que soma o conteúdo das linhas
    pivot_table['Total'] = pivot_table.count(axis=1)
    
    num_linhas = pivot_table.shape[0]
    
    # Ordena a tabela pelo total    
    return render_template('index_inventario_chamados.html', table=pivot_table.to_html(classes='table table-striped table-bordered'), num_linhas=num_linhas)
if __name__ == '__main__':
    app.run(debug=True)