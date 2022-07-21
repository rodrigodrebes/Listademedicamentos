import pandas as pd
arquivo = pd.read_csv('TA_PRECO_MEDICAMENTO.csv', encoding="ISO-8859-1", engine='python', sep=';')

def decisaoCodigo(): 
 nomeCodigo = (input("Digite o código de barras do medicamento: "))#solicita input do código de barras
 if (len(str(nomeCodigo))) != 13: #condição de tamanho do código de barras
     print("O código escolhido não é válido, tente novamente.") 
     return decisaoCodigo()#retorna a função
 else: 
     result = arquivo[arquivo['EAN 1'] == nomeCodigo]#mostra o resultado como string que pega do arquivo aquilo que for giual ao input
     print(result)#exibe o resultado

     pmcMax = result[['PMC 0%']].max().values[0]
     pmcMin = result[['PMC 0%']].min().values[0]
     print("O PMC máximo é", pmcMax)
     print("O PMC Mínimo é", pmcMin)
     print("A diferença entre o Maximo e o Mínimo é", (float(pmcMax.replace(",","."))-(float(pmcMin.replace(",",".")))))

decisaoCodigo()

#result = result[['PMC 0%']]#determina o escopo para a coluna de PMC 0%.