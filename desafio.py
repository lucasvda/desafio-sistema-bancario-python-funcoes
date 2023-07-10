menu = """

[1] Cadastrar Novo Usuário
[2] Cadastrar Nova Conta
[3] Listar Usuários
[4] Listar Contas
[5] Depositar
[6] Sacar
[7] Extrato
[8] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
#dados_usuarios = {}
dados_usuarios = {"38291661847":{"usuario_nome":"Lucas Venancio de Araujo", "usuario_nasc":"15/04/1990", "usuario_endereco":"Rua Aguanaval, 73 - Jardim Presidente - São Paulo/SP"}, "38291661857":{"usuario_nome":"Diego Dias Venancio de Araujo", "usuario_nasc":"19/06/1992", "usuario_endereco":"Rua Aguanaval, 73 - Jardim Presidente - São Paulo/SP"} }
contas = []
numero_conta = 0


def verificar_usuario(dados, cpf):
    if dados.get(cpf):
        return False
    else:
        return True

def cadastro_usuario(nome, data_nasc, cpf, endereco):
    usuario = {cpf:{"usuario_nome":nome, "usuario_nasc":data_nasc, "usuario_endereco":endereco}}
    return usuario[cpf]
    
def verificar_formatacao_data_nasc(data_nasc):
    if len(data_nasc) == 10 and data_nasc[2] == "/" and data_nasc[5] == "/":
        return True
    else:
        return print("Padrão de data incorreto, por favor digite o valor seguindo o padrão DD/MM/AAAA.") 
       
def verificar_formatacao_cpf(cpf):
    if len(cpf) == 11:
        return True
    else:
        return print("Padrão de CPF incorreto.")

def cadastrar_conta(cpf, numero_conta):
    nova_conta = [cpf, "0001", numero_conta + 1]
    return nova_conta

def verificar_conta_existente(cpf, lista_contas):
    numero_contas = 0
    if lista_contas == []:
        return numero_contas
    else:
        for lista in lista_contas:
            if lista[0] == cpf:
                numero_contas += 1
        return numero_contas
    
def listar_usuarios(lista_usuarios_cadastrados):
    numero_cliente = 0
    for lista in lista_usuarios_cadastrados:
        numero_cliente += 1       
        nome = lista_usuarios_cadastrados[lista]["usuario_nome"]
        nasc = lista_usuarios_cadastrados[lista]["usuario_nasc"]
        endereco = lista_usuarios_cadastrados[lista]["usuario_endereco"]
        print(f"Cliente Nº: {numero_cliente}\nNome: {nome}\nData de Nascimento: {nasc}\nEndereço: {endereco}\n\n")
        print(f"Titular das contas:\n")
        

def listar_contas(lista_contas_cadastradas):
    for lista in lista_contas_cadastradas:
        print(f"CPF: {lista[0]}\nAgência: {lista[1]}\nConta Corrente: {lista[2]}\n\n")
    
def deposito(saldo, valor, extrato,/):
    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            return saldo, extrato
    else:
       print("Operação falhou! O valor informado é inválido.")
       return saldo, extrato
    
def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            return saldo, extrato, numero_saques

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
            return saldo, extrato, numero_saques

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            return saldo, extrato, numero_saques

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            return saldo, extrato, numero_saques
        else:
            print("Operação falhou! O valor informado é inválido.")
            return saldo, extrato, numero_saques
        
def exibir_extrato(saldo, /, *,extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

while True:

    opcao = input(menu)

    if opcao == "1":
        nome = input("Insira o seu nome:\n")
        data_nasc = input("Insira sua data de nascimento nesse padrão DD/MM/AAAA:\n")
        if verificar_formatacao_data_nasc(data_nasc) != True:
            print("Por gentileza, faça o cadastro novamente.")
        else: 
            cpf = input("Insira o seu CPF sem pontuação:\n")
            if verificar_formatacao_cpf(cpf) != True:
                print("Por gentileza, faça o cadastro novamente.")
            else:
                logradouro = input("Isira o seu logradouro (rua, avenida e etc...):\n")
                numero = input("Isira o número da sua residência:\n")
                bairro = input("Isira o seu bairro:\n")
                cidade = input("Isira a sua cidade:\n")
                estado = input("Isira a sigla do seu estado:\n")
                endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"                
                if nome != "" and data_nasc != "" and cpf != "" and endereco != "":            
                    if verificar_usuario(dados_usuarios, cpf) == True:
                        dados_usuarios[cpf] = cadastro_usuario(nome, data_nasc, cpf, endereco)
                        print(f"Usuário {nome} cadastrado com sucesso!")
                    else:
                        print(f"CPF: {cpf} já existe, por favor digite um novo CPF.")      

    elif opcao == "2":
        cpf = str(input("Digite o CPF do usuário, sem pontuação, que deseja cadastrar a nova conta:\n"))
        if verificar_formatacao_cpf(cpf) != True:
                print("Por gentileza, faça o cadastro novamente.")
        elif verificar_usuario(dados_usuarios, cpf) == True:
            print("Esse CPF ainda não possuí cadastro, por gentileza faça o cadastro de usuário primeiro.")
        else:
            #numero_conta = verificar_conta_existente(cpf, contas)
            contas.append(cadastrar_conta(cpf, numero_conta))
            numero_conta += 1
            print(f"Conta cadastrada com sucesso!")

    elif opcao == "3":
        listar_usuarios(dados_usuarios)
    
    elif opcao == "4":
        listar_contas(contas)

    elif opcao == "5":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(saldo, valor, extrato)               

    elif opcao == "6":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == "7":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "8":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
