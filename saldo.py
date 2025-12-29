class Saldo_user():
    
    def __init__(self):
        self.saldo = 0.0
        
        
    def adicionar_saldo(self,valor):
        
        if valor <= 0:
            return " O valor precisar ser maior que R$ 0 ."
        
        self.saldo += valor
        return f"Saldo adicionado com sucesso. Novo saldo R$ {self.saldo:.2f}"
    
   