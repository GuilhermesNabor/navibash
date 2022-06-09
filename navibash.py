print('$=================Bem Vindo, NaborZin=================$')
from googlesearch import search

query = str(input('Digite a Pesquisa: '))

print()
result = list(
    search(
        query,
        lang='pt-br',
        num_results=5
    )
)
print(result)

print('$=================NaborZin Interactive=================$')