class concessionaria:
    def __int__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo

class carro(concessionaria):
    def carro1(self, preco, financiar):
        print(f"Todos os Carros custam {preco}")
        if financiar == "sim":
            self.modelo = input('qual modelo de veículo você deseja? ')
            self.cor = input('Qual cor você deseja?: ')
            print(f"Parabéns, você financiou um carro {self.modelo}, da cor {self.cor}")
        else:
            print("Você não financiou nenhum veículo, obrigado pela visita a nossa concessionaria")

class motociclieta(concessionaria):
    def motocicleta1(self, preco, financiar):
        print(f"Todas as motocicletas custam {preco}")
        if financiar == "sim":
            self.modelo = input('qual modelo de motocicleta você deseja?: ')
            self.cor = input('qual cor você deseja?: ')
            print(f"parabéns, você financiou uma motocicleta {self.modelo}, da cor {self.cor}")
        else:
            print("Você não financiou nenhum veículo, obrigado pela visita a nossa concessionaria")
