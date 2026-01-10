import re


email_cadastrados = set()
class user():
    def __init__(self):
        self.user_data = {
            "Nome" : str(input("Informe o seu nome :\n")),
            "Idade" : self.obter_idade_valida(),
            "Email" :  self.obter_email_valido()
            
        }
        
        
        
    def validar_email(self,email):
            if not email.endswith('@gmail.com'):
                return 'O E-mail deve ser do dominio @gmail.com. Tente novamente.'
            
            
            
            regex_email = "^[a-zA-Z0-9._%+-]+@gmail.com$"
            if not re.match(regex_email, email):
                return " E-mail no formato incorreto. Tente novamente. "
            

            
            
            limites_caracteres = 100
            
            if len(email) > limites_caracteres:
                return f" O E-mail deve ter no maximo {limites_caracteres} caracteres. Tente novamente."
            
            return email
        
        
    def  obter_email_valido(self):
        while True:
            
            email = str(input("\nInforme o seu E-mail : \n"))
            email_lower = email.lower()

            if email_lower in email_cadastrados:
                print( "❌ERROR: Esse email ja foi cadastrado! Tente outro.")
                continue
            

            validacao = self.validar_email(email)
            
            if validacao  ==  email:
                email_cadastrados.add(email_lower)
                return email
            
            else:
                print(validacao)
        
            
    def validar_idade(self,idade):
        if idade < 18:
            return "Você deve ter de 18 anos a mais para poder acessar o programa"
        return None

    def obter_idade_valida(self):
        while True:
            try:
                idade = int(input("\nInforme sua idade :\n"))
                
                validacao_idade = self.validar_idade(idade)
                
                if validacao_idade is None:
                    return idade
                
                else:
                    print(validacao_idade)
                    
            except ValueError:
                print("Por favor escreva  um número válido para idade. ")

