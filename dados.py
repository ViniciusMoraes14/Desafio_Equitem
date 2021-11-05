#Função que verifica se o cnpj é válido e registra o cliente!

import requests

CLIENTES = []
CNPJs = []

def registrar_cliente(cnpj):
    print()
    print('Deve ser digitado apenas os números do CNPJ para consulta!')
    print('EXEMPLO: 00000000000000')
    print()
    cnpj = input("Digite o CNPJ: ").upper()       #Parte 1 - Validação
    if cnpj not in CNPJs:
        if len(cnpj) == 14:
            consulta = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj))
            var = consulta.json()
        if {'status': 'ERROR', 'message': 'CNPJ inválido'} == var:
            print('cnpj inválido!')
            exit()
        if {'status': 'ERROR', 'message': 'CNPJ inválido'} != var:
            print(var)
    else:
        print('Cnpj Inválido!')
    
    if cnpj not in CNPJs:
        registro = input('Deseja registrar o cliente?\nDigite o número da operação!\n 1.Sim ou 2.Não?')  #Parte 2 - Registro
        if registro == '1':
            consulta = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj))
            new_client = consulta.json()
            NOME = new_client['nome']
            CNPJ = new_client['cnpj']
            RAZAO_SOCIAL = new_client['fantasia']
            Cliente = [NOME,CNPJ,RAZAO_SOCIAL]
            CNPJs.append(cnpj)
            CLIENTES.append(Cliente)
            print('Cliente registrado!')
        else:
            print('Voltando pro Menu!')
            return
    else:
        print('Cliente já cadastrado!')
