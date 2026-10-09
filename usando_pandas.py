import pandas as pd
import numpy as np

lista = [10,20,30]
print(print(f"\n{type(lista)}\n"))
array = np.array(lista)
print(f"\n{type(array)}\n")
lista_serie = pd.Series(array)
print(f"\n{type(lista_serie)}")

serie_index_personalizado = pd.Series(lista, index=["Alice", "bob", 'Charlie']) # passsa como parametro a LISTA e os labels que substituirão o indice numerico

print(serie_index_personalizado, end='\n \n')

print(serie_index_personalizado, end='\n \n')
# retorna o tipo de dado int64

idade_alice = serie_index_personalizado.Alice # requisitando o valor associado ao indice
print(idade_alice) 

serie_object = pd.Series(data=[100, 'egurt', 'jair', 2.718])
print(serie_object, end= "\n \n") # retorna o tipo de dado object pq nao tem um tipo dado unico

dicionario = {"a": 2, "b": 3, "c": 4, "d": 5}

serie_dict = pd.Series(dicionario)
print(serie_dict)



serie = pd.Series(data= [100,200,300,400,500], index=["a","b","c","d","e"])
media = serie.mean()
print(media)
mediana = serie.median()
print(mediana)
desvio_padrao = serie.std()
print(desvio_padrao)


valores_acima_da_media = serie[serie > serie.mean()]

quantidade_de_valores_acima_da_media = serie[serie > serie.mean()].count()

print(f"Valores acima da media: \n{valores_acima_da_media}\n")
print(f"Quantidade de Valores acima da media: \n{quantidade_de_valores_acima_da_media}\n")



print(f"lista com Valores dobrados: {list(map(lambda x:x*2, serie))}") # transformando em lista e iterando e multiplicando por 2
classdata = pd.read_csv('pandas-sample-data.csv')
print(classdata)
print(classdata.describe()) # traz o resultado das principais funcoes, como media mediana minimo maximo etc

classdata.rename(columns={
    "ID_Curso": "Identificação",
    "Instrutor": "Prof",
    "AE": "Fodase"
},inplace=True) # precisa desse inplcae para executar o update NA variavel e nao criar uma copia com essas modicações

classdata.rename(columns=lambda x: x.lower().replace(" ", "_"), inplace=True) # transforma TODAS colunas em minusculo e coloca _ no lugar de espacos
classdata.rename(index=lambda i: "Index_" + str(i), inplace=True) # substituindo o indice por uma string "Index_(i)"
print(classdata)