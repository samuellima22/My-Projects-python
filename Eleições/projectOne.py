class Urna:
    def __init__(self,numero1, numero2,candidato1 ='bolsonaro',candidato2='Lula'):
        self.candidato1 = candidato1
        self.candidato2 = candidato2
        self.numero1 = numero1
        self.numero2 = numero2

    def votar(self):
        v1 = input('Deseja fazer a votação?')
        if v1 == "sim":
            self.numero1 = '22'
            self.numero2 = '13'
            print(f'{self.candidato1}  ({self.numero1}) \n {self.candidato2}  ({self.numero2}) ')
            v2 = input('Digite o número do seu candidato: ')
            if v2 == self.numero1:
                print('Voto efetuado com sucesso')

            elif v2 == self.numero2:
                print('Voto efetuado com sucesso')

            else:
                while v2:
                    print('Não existe nenhum candidato com esse numero, tente novamente')
                    break



        elif v1 == "não":
            print("Você optou por não votar, até a próxima eleição ;)")
