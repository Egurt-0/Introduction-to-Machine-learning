import numpy as np

matriz =[ 
    
    [1,2,3,4,5],
    [6,7,8,9,10,],
    [11,12,13,14,15]

]


print(matriz[2][:]) # coluna 2 e um slice na linha
# slice (:) pega todos os elementos

print(matriz[0][1::2]) # slice com step
# STEP (1::) siginfica como ITERO os dados, nesse caso de dois em dois começando pelo indidce 1


array_2d = np.array([[10,11,12,13,14],
                     [20,21,22,23,24],
                     [30,31,32,33,34]])


slice_com_step = array_2d[1, 0:4:2] # pega a coluna de indice 1 e comeca no item 0 tem como limite o 3 (4-1) e pula de dois em dois
print(f"\n {slice_com_step} \n")

array_linear = np.linspace(0,1,5) # array que vai de  0 a 1 e tem 5 elementos
print(array_linear)


soma_das_COLUNAS = array_2d.sum(axis=0) # pega todas as linhas e soma e forma uma array novo com o resultado da soma de cada linha
soma_das_LINHAS = array_2d.sum(axis=1) # pgea todas as coluna e soma e forma um array novo com o resutlado de cada coluna
media_das_COLUNAS = array_2d.mean(axis=0) # mesma coisa só que media ao inves de soma
media_das_LINHAS = array_2d.mean(axis=1) # mesma coisa só que media ao inves de soma

print(f"\n{soma_das_COLUNAS}\n")
print(f"\n{soma_das_LINHAS}\n")

print(f"\n{media_das_COLUNAS}\n")
print(f"\n{media_das_LINHAS}\n")


array_1d = np.arange(100) # cria uma array de 10 elementos e 10 indices
print(array_1d)
array_50x2 = array_1d.reshape(2,50) # converto o array anterior em um array 50x2 (nao adianta colocar qualquer valor, precisa ser possivel fazer a divisao)
print(f"\n\n{array_50x2}\n\n")
array_2Xseila = array_1d.reshape(2, -1) # converte para um array de 5 linhas e quantas colunas FOR NECESSARIO
print(array_2Xseila)
meu_array = np.array(matriz)
print(type(meu_array))
print(meu_array.shape)

array_concat = np.concatenate((array_1d, array_linear))
print(array_concat)
print(np.zeros(6).shape) # instancia uma lista com x zeros, nesse caso 6

