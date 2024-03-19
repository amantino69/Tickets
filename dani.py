import os
import fileinput


diretorio = r'C:\Users\Regina Casoti\Documents\Matheus'

texto_antigo = '2023'
texto_novo = '2024'

# Percorre todos os arquivos no diretório
for root, dirs, files in os.walk(diretorio):
    for file in files:
        # Abre o arquivo em modo de leitura e escrita
        with fileinput.FileInput(os.path.join(root, file), inplace=True) as f:
            # Substitui o texto antigo pelo novo em cada linha do arquivo
            for line in f:
                print(line.replace(texto_antigo, texto_novo), end='')

