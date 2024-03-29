# -*- coding: utf-8 -*-
"""Projeto Custos Produção_OAC_v_final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P2b-O4RpCthYrg5ahl_MtbZ9_UCzFfxX

### **PROJETO CUSTOS DE PRODUÇÃO **

Neste projeto é feita a concatenação de mais de 30 planilhas com doze culturas agrícolas de inverno e verão. Como resultado, temos um único dataframe com a série histórica de todas as culturas analisadas.
"""

from google.colab import drive
drive.mount('/content/drive')

# Passo 1: importar os pacotes necessários
import os
import pandas as pd
import plotly.express as px

# Passo 2:  Definir uma variavel para o nome do caminho onde estão as planilhas, ou seja, a pasta onde estão:
path = r'/content/drive/MyDrive/2. Projetos de ciência de dados/Custo Ref. Produção - Tratamento de dados/2. Planilhas de custo por mes e ano '
# obs: o "r" serve para ajustar as barras do endereço a ser buscado, facilitando o trabalho.

# Passo 3: Definir uma lista de todos os arquivos existentes na pasta especificado e criar um dataframe em branco, onde serão, posteriormente, acomodados os dados de todas as planlhas.
files = os.listdir(path)

df = pd.DataFrame()

display(files)

# Passo 4: Agora, vamos denominar os caminhos específicos de cada um dos arquivos da pasta onde estão todas as planilhas, ou seja, da pasta denominada "path"
# Chamaremos de "files_xlsx" e buscaremos apenas os arquivos com a extensão "xlsx":
files_xslx= [path + '/' + f for f in files if f [-4:] =='xlsx']

print("Arquivos em '", path, "':")

display(files_xslx)

# Passo 5: Agora, vamos criar uma variavel chamada "data", que irá fazer a leitura, em excel, de cada uma dos arquivos chamados files_xlsx.
# Iremos ler apenas os arquivos que possuem "Custo_referencial" no nome:

for f in files_xslx:
  if "Custo_referencial" in f:
    data = pd.read_excel(f)
    display(data)
    # Na sequência, iremos concatenar as planilhas em excel, denominadas "data", com o DataFrame (df) que foi criado anteriormente e está pronto para receber os dados:
    # Aqui, ordenamos a tabela pela coluna dat_ano, de forma decrescente:
    df = pd.concat([df,data]).sort_values(by="nom_produto", ascending=True)

# Passo 6: Agora, vamos plotar a nova tabela df, que acomoda todos os dados de cada uma das planihas.
display(df)

import datetime
#Por último, iremos adicionar uma coluna chamada "data", em formato data no df:
df['dat_ano'] = df['dat_ano'].astype(str)
df['dat_mes'] = df['dat_mes'].astype(str)
df['data'] = '01/'+ df['dat_mes'] + '/' + df['dat_ano']

display(df)

# Passo 7: Exportar df para excel:
df.to_excel('Base_custo_referencial_v2.xlsx')

