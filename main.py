import pandas as pd
import os
from pathlib import Path
from openpyxl import Workbook


# os.system('cls')

while True:
    print("""
    [0] Criar um Arquivo  
    [1] Adicionar uma Coluna
    [2] Adicionar uma Linha
    [3] Remover um Linha ou Coluna
    [4] Editar uma Linha
    [5] Fazer um Backup
    [6] Importar 
    [7] Sair """)

    Escolhas = int(input("Escolha um numero de 0 a 5: "))
    if Escolhas == 0:
        os.system('cls')
        name = str(input("Digite o nome da tabela: "))
        wb = Workbook()
        sheet = wb.active
        wb.save(f'{name}.xlsx')
        break

    if Escolhas > 0:
        Caminho = str(input("Digite o caminho aqui: "))
        if Escolhas == 1:
            df = pd.read_excel(f"{Caminho}")

            Coluna = str(input("Adicionar uma Coluna: "))
            df[Coluna] = []

            df.to_excel(f"{Caminho}", index=False)
            print("Coluna Adicionada Com Sucesso")

        elif Escolhas == 2:
            tabela = pd.read_excel(Caminho)
            dataFrame = pd.DataFrame(tabela)
        elif Escolhas == 3:
            print("Escolha 3")
        elif Escolhas == 4:
            print("Escolha 4")
        elif Escolhas == 5:
            print("Escolhas ")
        elif Escolhas == 6:
            print("Escolhas")
        elif Escolhas == 7:
            print("FIM")
            break
