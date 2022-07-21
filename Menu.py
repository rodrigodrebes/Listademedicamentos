# importação de bibliotecas
import pandas as pd
import re
# define "arquivo" como variável de leitura do CSV. Isso permite que acessemos mais rápido o documento.
arquivo = pd.read_csv('Programa\TA_PRECO_MEDICAMENTO.csv', encoding="ISO-8859-1", engine='python', sep=';')


def menuPrincipal():  # primeiro menu de decisão, entre Lista de crédio e Consulta de medicamento
    print("PARA CONTINUAR, SIGA AS OPÇÕES ABAIXO:"
          """
 Opções:
 1 - Lista de Concessão de Créditos Tributários
 2 - Lista de medicamentos
 9 - Sair do programa
 Qual você deseja consultar?
 """)

    decisao1 = int(input(" "))  # solicita input para o menu

    if decisao1 == 1:  # se o input for 1, em relação a Concessão de Créditos, exiba:
        listaCreditos()

    elif decisao1 == 2:  # se o input for 2, em relação à Lista de Medicamentos, exiba:
        menuSecundario()  # Se a decisão for por busca de medicamento, especifique

    elif decisao1 == 9:
        print("Caso queira consultar novamente, basta reabrir o programa! Adeus!")
        import sys
        sys.exit()


def listaCreditos():  # função que define a escolha da Lista de Concessão de Créditos Tributários
 comercializados2020 = arquivo[arquivo['COMERCIALIZAÇÃO 2020'] == 'Sim'] # define o escopo da busca somente para os medicamentos comercializados em 2020
 porcentagem = (comercializados2020['LISTA DE CONCESSÃO DE CRÉDITO TRIBUTÁRIO (PIS/COFINS)'].value_counts(normalize=True) * 100)  #mostra a porcentagem dos dados, referente à coluna Lista de Créditos
 classificacao = [] #cria array vazio para receber os dados de classificação
 porcentagens = [] #cria array vazio para receber os dados de porcentagens
 asteriscos = [] #cria array vazio para receber os dados de asteriscos
 asteriscostring = ""  #cria string vazio para receber os dados de asteriscos

 for i in porcentagem.index: #em cada repetição ele vai acrescentar as classificações ao array de classificação
    classificacao.append(i)

 for i in porcentagem:  #adiciona porcentagens ao array de porcentagens 
    porcentagens.append(i)
    for j in range(int(i)): #o código vai percorrer o número de asteriscos necessários, para poder adicionar na string vazia de asteriscos
      asteriscostring += "*"
    asteriscos.append(asteriscostring)
    asteriscostring = "" #a cada repeticao é zerado para iniciar novamente a contagem de asteriscos
   
 porcentagens.append("100%") #acrescenta a porcentagem total ao fim
 classificacao.append("TOTAL") #acrescenta a string TOTAL ao fim 
 asteriscos.append("") ##acrescenta uma string vazia ao fim 

 dados = {'Classificação':  classificacao, 'Porcentagem': porcentagens, 'Gráfico': asteriscos} #criação de um dataframe para armazenagem e tratamento dos dados 
 df = pd.DataFrame(dados) 
 print("A lista de concessão de créditos tributários, somente para medicamentos comercializdos no ano de 2020, é a seguinte: \n\n") #exibe os resultados
 print(df)
 import sys
 sys.exit()


def menuSecundario():  # função que define o menu secundário, sobre medicamentos
    print("""
 Opções:
 1 - Consultar a Lista de medicamentos por nome ou abreviação
 2 - Consulta de medicamento por código de barras
 9 - Voltar
 Qual você deseja? 
 """)
    decisao2 = int(input(" "))  # solicita input do usuário
    if decisao2 == 1:  # se a decisão for para buscar por nome, faça:
        decisaoNome()

    elif decisao2 == 2:  # se a decisão for para busca pelo código, faça:
        decisaoCodigo()

    elif decisao2 == 9:  # se a decisão for para voltar ao menu anterior, faça:
        menuPrincipal()  # Problema: como voltar para o menuPrincipal e repetir todas as consequências acima? (decisao1, decisao2, etc.)


def decisaoNome():
    # define o escopo da busca somente para os medicamentos comercializados em 2020
    comercializados2020 = arquivo[arquivo['COMERCIALIZAÇÃO 2020'] == 'Sim']
    # input do nome do medicamento
    nomeMedicamento = str(input("Digite do nome medicamento desejado, em letras maiúsculas: "))
    result = comercializados2020[comercializados2020['SUBSTÂNCIA'].str.contains(nomeMedicamento)]
    # Exibe a Substância, Produto, Apresentação e PF Sem Imposto.
    print("\n\n Para medicamentos comercializados em 2020 com esta nomeclatura, encontramos os seguintes resultados: \n\n ", result[['SUBSTÂNCIA', 'PRODUTO', 'APRESENTAÇÃO', 'PF Sem Impostos']])
    print("""\n
 Deseja buscar outro medicamento ou retornar ao menu principal?
 1 - Escolher outro medicamento
 2 - Retornar ao menu Principal
 9 - Sair do Programa 
 """)
    escolhaAposCodigo = int(input(
        " "))  # input para retornar ao menu principal ou procurar por outro medicamento
    if escolhaAposCodigo == 1:
        menuSecundario()
    elif escolhaAposCodigo == 2:
        menuPrincipal()
    elif escolhaAposCodigo == 9:
        print("Caso queira consultar novamente, basta reabrir o programa! Adeus!")
        import sys
        sys.exit()


def decisaoCodigo(): 
 nomeCodigo = (input("Digite o código de barras do medicamento: "))#solicita input do código de barras
 if (len(str(nomeCodigo))) != 13: #condição de tamanho do código de barras
     print("O código escolhido não é válido, tente novamente.") 
     return decisaoCodigo()#retorna a função
 else: 
     result = arquivo[arquivo['EAN 1'] == nomeCodigo]# pega do arquivo aquilo que for giual ao input
     print(result)#exibe o resultado

     pmcMax = result[['PMC 0%']].max().values[0]#determina o PMC máximo, pegando somente o valor
     pmcMin = result[['PMC 0%']].min().values[0]#determina o PMC mínimo, pegando somente o valor
     print("O PMC máximo é", pmcMax)#exibe o resultado
     print("O PMC Mínimo é", pmcMin)#exibe o resultado
     print("A diferença entre o Maximo e o Mínimo é", (float(pmcMax.replace(",","."))-(float(pmcMin.replace(",",".")))))# em razão de erro comparativo entre str e float, passei para float o resultado
    
     print("""\n
 Deseja buscar outro medicamento ou retornar ao menu principal?
 1 - Escolher outro medicamento
 2 - Retornar ao menu Principal
 9 - Sair do Programa 
 """)
 escolhaAposCodigo = int(input(
        " "))  # input para retornar aos menus ou procurar por outro medicamento
 if escolhaAposCodigo == 1:
        menuSecundario()
 elif escolhaAposCodigo == 2:
        menuPrincipal()
 elif escolhaAposCodigo == 9:
        print("Caso queira consultar novamente, basta reabrir o programa! Adeus!")
        import sys
        sys.exit()

# início de execução do código
menuPrincipal()  
