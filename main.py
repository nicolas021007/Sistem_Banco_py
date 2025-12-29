from menu_usuario import  user
from saldo import Saldo_user
from verify import Verificar_dados

usuario_cadastrado = None
saldo_atual = None

class main():
    pass

print("Olá seja  bem-vindo(a) ao seu banco")
while True:
    

    print("------ MENU PRINCIPAL ------ \n")     

    print("(1) Cadastrar usuário.")
    print("(2) Colocar mais saldo na conta.")
    print("(3) Verificar quanto de saldo possui na conta.")
    print("(4) Todos os dados do usuário.")
    print("(5) Sair.")

    try:
        opcao = int(input("Escolha uma dessas opções:\n"))
        
    except ValueError:
        print("Erro: Usuário digitou um valor invalido! \n")
        continue

    if opcao == 1:
        usuario_cadastrado =  user()
        saldo_atual = Saldo_user()
        print(usuario_cadastrado.user_data)
        
    elif opcao == 2:
        if usuario_cadastrado is None:
            print("ERROR : Por favor, cadastre-se primeiro na opção 1.\n")
            
        else:
           try:
               valor = float(input("\n Informe o valor que deseja adicionar ao saldo :"))
               mensagem = saldo_atual.adicionar_saldo(valor)
               
               print(mensagem)
           except ValueError:
               print("ERROR : Por favor, digite um valor numério válido.\n")
               
    elif opcao == 3:
        if usuario_cadastrado is None :
            print("ERROR : Por favor, cadastre-se primeiro na opção 1. \n")

        elif saldo_atual is None:
            print("ERROR : Por favor, adicione saldo na opção 2. \n")
            
        else:
            print(f"Seu saldo atual é de R$ {saldo_atual.saldo} \n")
            
    
    elif opcao == 4:
        if usuario_cadastrado is None :
            print("ERROR : Por favor, cadastre-se primeiro na opção 1. \n")    
        
        elif saldo_atual is None :
            print("ERROR : Por favor, adicione saldo na opção 2. \n")    
        
        else:
            dados = Verificar_dados(usuario_cadastrado, saldo_atual)
            dados.exibir_dados()
    elif opcao == 5:
        print("Obrigado pela atenção! Volte sempre.")
        break
            
