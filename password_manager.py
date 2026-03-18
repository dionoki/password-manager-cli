#Início primeiro projeto ( Sistema de gerenciamento de senhas com hash )
import json

#Dados, arquivos ---------------------------------------------------------------------------------------------------------------------------------------------------------
def salvar_dados():
  geral = {
     "senha_mestre": senha_mestre,
     "dados": dados
    }
  with open('arquivo.json', 'w', encoding='utf-8') as arquivo:
   json.dump(geral, arquivo, indent=4)      

def carregar_dados():
    with open("arquivo.json", "r") as arquivo:
      geral = json.load(arquivo)
      return geral["senha_mestre"], geral['dados']
 

#Dicionário -----------------------------------------------------------------------------------------------------------------------------------------------------------------

try: 
  senha_mestre, dados = carregar_dados()
except:
  senha_mestre = "1109"
  dados = {
    'gmail': {
        'login': 'usuario@gmail.com',
        'senha': '32'},
    'netflix': {
        'login': 'usuario.netflix',
        'senha': '123456789'}}

 # Função principal do codigo ------------------------------------------------------------------------------------------------------------------------------------------------

def mostrar_servicos(senhas):
    print('Serviços Disponíveis:')
    for servico in senhas:
        print('- ' + servico)

def pedir_servico():
   servico = input("Selecione um serviço: ").strip().lower()
   return servico

def autenticar():
 senha = input('Digite a senha: ').strip()
 return senha == senha_mestre
 
def mostrar_dados(servico, dados):
     print('Serviço encontrado!')
     print("login:", dados[servico]['login'])
     print("senha:", dados[servico]['senha'])
     
# Sistema principal ---------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    mostrar_servicos(dados)
    servico = pedir_servico()

    if servico in dados:

      if autenticar():
            mostrar_dados(servico, dados)
      else:
            print('Acesso negado')
      break
    else:
        print('Serviço não encontrado!')

salvar_dados()

