import http.client
import json
import pandas as pd

# Está função consulta a API do ViaCEP para obter informações de endereço com base em um CEP
def obter_endereco_por_cep(cep):

    conexao = http.client.HTTPSConnection("viacep.com.br") # Cria a conexão HTTPS com o viacep. E o HTTPS garante os dados enviados e recebidos sejam criptografados para segurança
    conexao.request("GET", f"/ws/{cep}/json/") # Requisição GET que inclui o CEP fornecido na URL
    resposta = conexao.getresponse() # Aguarda a resposta. E o metodo 'getresponse' retorna um objeto que representa a resposta HTTP

    # Verifica se teve sucesso(200) ou não no status da resposta
    if resposta.status != 200:
        conexao.close()
        return None
    
    dados = resposta.read() # Le os dados da resposta
    endereco = json.loads(dados.decode("utf-8")) # Decodifica os bytes recebidos para o formato UTF-8
    conexao.close() # Encerra conexão HTTPS
    return endereco if "erro" not in endereco else None

caminho_planilha = "CEP.xlsx"
planilha_cep = pd.read_excel(caminho_planilha, sheet_name='CEP')
ceps = planilha_cep['CEP'].dropna()
resultados = pd.DataFrame(columns=['CEP', 'Logradouro', 'Bairro', 'Localidade', 'UF', 'DDD'])

for cep in ceps:
    endereco = obter_endereco_por_cep(str(cep).replace('-', ''))
    
    if endereco:
        nova_linha = pd.DataFrame([{
            'CEP': cep,
            'Logradouro': endereco.get('logradouro', ''),
            'Bairro': endereco.get('bairro', ''),
            'Localidade': endereco.get('localidade', ''),
            'UF': endereco.get('uf', ''),
            'DDD': endereco.get('ddd', '')
        }])
        resultados = pd.concat([resultados, nova_linha], ignore_index=True)

with pd.ExcelWriter(caminho_planilha, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    resultados.to_excel(writer, sheet_name='Dados', index=False)

print("Endereços salvos na aba 'Dados' na planilha 'CEP.xlsx'")