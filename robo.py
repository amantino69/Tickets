from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    cpf = request.form['cpf']
    nome = request.form['nome']
    idade = request.form['idade']
    sexo = request.form['sexo']

    # Aqui você pode fazer o que quiser com os dados do formulário
    print(f'CPF: {cpf}, Nome: {nome}, Idade: {idade}, Sexo: {sexo}')

    return 'Formulário submetido com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)