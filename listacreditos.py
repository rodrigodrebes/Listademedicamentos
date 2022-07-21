import pandas as pd
arquivo = pd.read_csv('TA_PRECO_MEDICAMENTO.csv', encoding="ISO-8859-1", engine='python', sep=';')

def listaCreditos():  # função que define a escolha da Lista de Concessão de Créditos Tributários
 comercializados2020 = arquivo[arquivo['COMERCIALIZAÇÃO 2020'] == 'Sim'] # define o escopo da busca somente para os medicamentos comercializados em 2020
 porcentagem = (comercializados2020['LISTA DE CONCESSÃO DE CRÉDITO TRIBUTÁRIO (PIS/COFINS)'].value_counts(normalize=True) * 100)  #mostra a porcentagem dos dados, referente à coluna Lista de Créditos

 classificacao = []
 porcentagens = []

 for i in porcentagem.index:
    classificacao.append(i)

 for i in porcentagem:
    porcentagens.append(i)

 data = {'Classificação':  classificacao, 'Porcentagem': porcentagens}
         
        
       #criação de um dataframe para armazenagem e tratamento dos dados
 df = pd.DataFrame(data)

 #for i in porcentagem.index:
      # print(i)
       #print(porcentagem)

 print("A lista de concessão é a seguinte: ") #exibe os resultados
 print(df)
 import sys
 sys.exit()

listaCreditos()


#porcentagem = porcentagem.reset_index()  # make sure indexes pair with number of rows 
#for index, row in df.iterrows():


#criar um dataFrame

