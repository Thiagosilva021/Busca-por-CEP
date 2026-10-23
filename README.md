# BuscaCEP

Projeto simples em Python que consulta a API do
[ViaCEP](https://viacep.com.br/) para buscar informações de endereço a
partir de uma lista de CEPs armazenada em uma planilha Excel.

## Funcionalidades

-   Lê CEPs de uma planilha Excel.
-   Consulta o ViaCEP para obter os dados de cada CEP.
-   Coleta logradouro, bairro, localidade, UF e DDD.
-   Salva os resultados em uma aba chamada `Dados` no arquivo Excel.

## Tecnologias utilizadas

-   **Python**
-   **Pandas** --- leitura e escrita de planilhas.
-   **HTTP client** (`http.client`) --- requisições HTTP à API.
-   **JSON** --- processamento das respostas da API.
-   **OpenPyXL** --- mecanismo utilizado pelo Pandas para editar
    arquivos `.xlsx`.

## Pré-requisitos

Tenha o Python instalado e instale as bibliotecas necessárias:

``` bash
pip install pandas openpyxl
```

## Como preparar a planilha

Crie um arquivo chamado `CEP.xlsx` na mesma pasta do notebook. Ele deve
conter uma aba chamada `CEP` e uma coluna chamada `CEP`, com um código
postal por linha.

Exemplo:

  CEP
  ----------
  01001000
  20040002
  30140071

Mantenha os CEPs como texto, se possível, para preservar zeros à
esquerda.

## Como executar

1.  Coloque `buscaCEP.py` e `CEP.xlsx` na mesma pasta.
2.  Abra o códigoem um ambiente compatível.
3.  Execute o código no terminal usando o comando  `python .\buscaCEP.py`.
4.  Após a execução, confira a aba `Dados` no arquivo `CEP.xlsx`.

A aba `Dados` conterá as colunas:

-   `CEP`
-   `Logradouro`
-   `Bairro`
-   `Localidade`
-   `UF`
-   `DDD`

Se a aba `Dados` já existir, ela será substituída pelos novos
resultados. O arquivo precisa existir e não deve estar aberto no Excel
durante a gravação.

## Tratamento de CEPs

O código ignora CEPs vazios e não adiciona aos resultados os CEPs para
os quais a API retorna erro ou que não são encontrados.

## Observações

-   É necessária uma conexão com a internet para consultar a API.
-   A disponibilidade e as informações retornadas dependem do serviço
    ViaCEP.
-   O caminho `CEP.xlsx` é relativo à pasta de execução. Se o arquivo
    estiver em outro local, ajuste a variável `caminho_planilha`.
