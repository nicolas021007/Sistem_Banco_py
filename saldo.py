class Saldo_user():
    
    def gestao_saldo(self):
        while True:
            print("\n -------- GESTÃO DE SALDO --------\n")
            print("(1) -  Depositar saldo.")
            print("(2) -  Sacar saldo.")
            print("(3) -  Sair.\n")
            
            opcao = int(input("Escolha uma dessas opções : \n"))
            
            if opcao == 1:
                self.depositar()
                
            elif opcao == 2 :
                self.sacar()
                
            elif opcao == 3:
                break
            
            

    def __init__(self, saldo_inicial = 0):
        
        self.saldo = saldo_inicial
        
    def depositar(self):
        try:
            valor = float(input("Informe a quantidade de saldo que deseja depositar : \n"))
        
            if valor > 0:
                self.saldo += valor
                print("\n-------- ✅ Depósito Realizado --------\n ")
                print(f" Saldo atual : R${self.saldo:.2f}\n")
            
        except ValueError:
         return "❌ERROR : Por favor digite um número válido."
     
        
    def sacar(self):
        try:
            
            valor = float(input("Informe o valor que deseja sacar : \n"))

            if valor < 0 :
                return "❌ERROR : Valor invalido.\n "
        
            elif valor > self.saldo :
                return " ❌ERROR : Saldo insuficiente.\n"
        
            else:
                self.saldo -= valor
                print(f"\n-------- ✅Saque Realizado! --------\n ")
                print("Saldo atual : R${self.saldo:.2f}\n")
            
        except ValueError:
            return "❌ERROR : Digite um número válido"
     
    
   