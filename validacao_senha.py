import json

with open('senha.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

email = input("digite seu email: ")
senha = input("digite sua senha: ")

if email == dados['email'] and senha == dados['senha']:
    print("acesso liberado!")

else:
    print('acesso negado!')