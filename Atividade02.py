#1.	Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares.
def filtrar_impares(lista):
    return [num for num in lista if num % 2 != 0]

# Exemplo
print(filtrar_impares([1, 2, 3, 4, 5, 6])) # Saída: [1, 3, 5]

#2. Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes. 
def filtrar_primos(lista):
    def eh_primo(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True
    return [num for num in lista if eh_primo(num)]

# Exemplo
print(filtrar_primos([2, 3, 4, 5, 10, 11])) # Saída: [2, 3, 5, 11]

#3. Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas.
def elementos_unicos(lista1, lista2):
    set1, set2 = set(lista1), set(lista2)
    return list(set1.symmetric_difference(set2))

# Exemplo
print(elementos_unicos([1, 2, 3], [2, 3, 4])) # Saída: [1, 4]

#4. Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista. 
def segundo_maior(lista):
    unicos = list(set(lista))
    if len(unicos) < 2: return None
    unicos.sort()
    return unicos[-2]

# Exemplo
print(segundo_maior([10, 20, 20, 4, 45, 99])) # Saída: 45

#5. Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das pessoas em ordem alfabética.
def ordenar_por_nome(lista_pessoas):
    return sorted(lista_pessoas, key=lambda x: x[0])

# Exemplo
pessoas = [("Daniel", 40), ("Ana", 25), ("Bruno", 20)]
print(ordenar_por_nome(pessoas)) # Saída: [('Ana', 25), ('Bruno', 20), ('Daniel', 40)]

#6. Como identificar e tratar outliers em uma coluna numérica usando desvio padrão ou quartis?
#Outliers são valores que fogem drasticamente do padrão da distribuição.Desvio Padrão: Considera-se outlier valores além de 3 desvios padrões da 
#média ($media \pm 3 \times std$).Quartis (IQR): Calcula-se o Intervalo Interquartil ($IQR = Q3 - Q1$). 
#Outliers estão abaixo de $Q1 - 1.5 \times IQR$ ou acima de $Q3 + 1.5 \times IQR$.Tratamento:
#Podem ser removidos, substituídos pela média/mediana ou "capados" nos limites calculados.


#7. Como concatenar vários DataFrames (empilhando linhas ou colunas), mesmo que tenham colunas diferentes? Dica: Utiliza-se pd.concat() especificando axis=0 (linhas) ou axis=1 
#(colunas). Quando há colunas diferentes, os valores ausentes são preenchidos com NaN. 

#Utiliza-se a função pd.concat().
#Eixo 0 (Linhas): Empilha um DataFrame abaixo do outro.
#Eixo 1 (Colunas): Coloca um ao lado do outro.
#Colunas Diferentes: Se um DataFrame possui uma coluna que o outro não tem, o Pandas cria a coluna e preenche os espaços vazios com NaN (Not a Number).

#8. Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?  
import pandas as pd
df = pd.read_csv('arquivo.csv')
print(df.head()) # Exibe as 5 primeiras linhas por padrão

#9. Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?
# Selecionar coluna
coluna_idade = df['idade']

# Filtrar linhas (ex: pessoas com mais de 18 anos)
filtro = df[df['idade'] > 18]

#10. Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame? 
#Existem três abordagens principais no Pandas:

#Identificar: df.isnull().sum() para ver onde faltam dados.

#Remover: df.dropna() exclui linhas ou colunas com valores nulos.

#Preencher: df.fillna(valor) substitui os NaN por um valor fixo, pela média ou pela mediana da coluna.
