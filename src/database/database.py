import csv
import os 


ARQUIVO_JSON = 'database/financeiro.json'

usuarios = {
    'nome' : nome,
    'categoria' : categoria,
    'descricao' : descricao,
    'valor' : valor 
}


def inicializar_csv(ARQUIVO_CSV):
    if not os.path.exists(ARQUIVO_JSON): 
        with open(ARQUIVO_JSON, mode='w', newline='', encoding='utf-8') as json:
            escritor = json.writer(ARQUIVO_JSON)
            escritor.writerow(['nome', 'categoria', 'descricao', 'valor'])

        with open(ARQUIVO_JSON, mode='r', newline='', encoding='utf-8') as json:
            leitor = json.read(ARQUIVO_JSON)
            for linha in leitor:
                print(linha)



            


    




