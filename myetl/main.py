from extracty import ApiExtracty

class IntoFood:
    def __init__(self):
        self.name_pacient = str(input("Qual é nome do paciente? "))
        self.list_id = []

    def menu_food(self):
        while True:
            try:
                idtaco = int(input("Insira o ID do alimento: "))
                self.list_id.append(idtaco)
                objeto = ApiExtracty(self.list_id, self.name_pacient)
                for desc_food in objeto.taco_food():
                    print(desc_food['description'])
                resp = ' '
                while resp not in 'SN':
                    resp = str(input('Deseja adicionar outro alimento: [S/N]')).strip().upper()[0]
                if resp == 'N':
                    break
            except ValueError:
                print("Digite o ID novamente! ")
        return self.list_id

    def process(self):
        objeto = ApiExtracty(self.list_id, self.name_pacient)
        return objeto.generate_csv()


if __name__ == "__main__":
    objeto = IntoFood()
    objeto.menu_food()
    objeto.process()