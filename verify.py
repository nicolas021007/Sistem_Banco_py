class Verificar_dados():
    
    def __init__(self, usuario, saldo):
        
        self.usuario = usuario
        self.saldo =saldo
        
    def exibir_dados(self):
        if self.usuario and self.saldo:
            print("-------DADOS USUÁRIO-------\n")
            print(f"Nome : {self.usuario.user_data['Nome']}\n")
            print(f"Idade :{self.usuario.user_data['Idade']}\n")
            print(f"E-mail : {self.usuario.user_data['Email']}\n")
            print(f"Saldo : R$ {self.saldo.saldo : .2f} \n")