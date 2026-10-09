import pandas as pd
import numpy as np

dataframe_simples = pd.DataFrame(data=[ [1,'egurt'],
                                [10,"RAFA"], 
                                [-1,"EGURTO"]],
                                columns=["ID","nome"], index=["foda","lixo","sigma"])
print(dataframe_simples)

dados = {
    "id": [0,1,2],
    "nome": ["dudu", "eguro", "giulberto"],
    "idade": [16,15,22]
}
dados_dataframe = pd.DataFrame(data=dados, index=["primeiro","segundo","terceiro"])
print(dados_dataframe)

# ADICIONANDO COLUNA
dados_dataframe['Salario'] = [100000,220,2]
print(dados_dataframe)

# DATA FRAME COMPLEXOS

dataframe_complexo = pd.DataFrame(data={

    "Unidade": pd.Series([1,2,3,4,5]),
    "Dezena": pd.Series([10,20,30,40,50]),
    "Centena": pd.Series([100,200,300,400,500]),
    "de 0 a 1": np.linspace(0,1,5),
    "date": pd.date_range(start='1/1/2026', periods=5, freq='D')
})
array_egurt = np.array(dataframe_complexo)
juncao = np.append(array_egurt,array_egurt, axis=1)
print(juncao)
print(dataframe_complexo)

exerciciozinho = pd.DataFrame(data=[[1,2],[3,4],[5,6]] , # matriz 3x2
                              columns=["Egurt","skibidi"],
                              index=["um", "dois", "tres"])
print(exerciciozinho)