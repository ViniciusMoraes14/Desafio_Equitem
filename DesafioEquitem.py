from dados import registrar_cliente,CLIENTES,CNPJs

while True:
  print()
  print('Olá,Bem-Vindo!')
  print('Quais opções deseja navegar?\n   1.Exibir todos os clientes cadastrados\n   2.Adicionar um novo cliente\nDigite X - Se não quiser fazer mais nada!')
  print("-"*60)
  operacao = input('Digite o número da opção que deseja navegar: ').upper()
  if operacao == "X":
      break
  if operacao == "1":
    if len(CLIENTES) == 0:
      print("-"*60)
      print("Ainda não temos clientes cadastrados no nosso banco de dados!")
      print("-"*60)
    else:
      print('Todos os CNPJs cadastrados!')
      print("*"*60)
      count = 1
      for x in CLIENTES:
        print(f'CLIENTES-{count}: {x}')
        count+=1
        print("-*-*"*60)
  elif operacao == "2":
    registrar = input('Deseja verificar o cnpj?\n Digite o número da operação!\n 1.SIM ou 2.NÃO?: ').upper()
    if registrar == '1':
      registrar_cliente(CNPJs)
      print()
    else:
        print('Voltando pro Menu!')
    
