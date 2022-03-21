from typing_extensions import Literal
import requests
import json
import pandas as pd


class tacoApi:
    def __init__(self):
        self.name_patient = str(input('Qual é nome do seu paciente? '))
        self.list_food = []
        self.list_id = []
        while True:
            idtaco = int(input('Insira o id do Alimento: '))
            url = requests.get(f"http://localhost:4000/api/v1/food/{idtaco}/")
            self.list_id.append(url.json())
            resp = ' '
            while resp not in 'SN':
                resp = str(input('Deseja adicionar outro alimento: [S/N]')).strip().upper()[0]
            if resp == 'N':
                break


    def taco_food(self):
        def normalize(attributes):
            if type(attributes) == float:
                new_value = f"{attributes:.1f}"
            else:
                new_value = attributes
            return new_value.replace('.', ',')


        def macro_not_exist(food):
            list_macro = ['protein', 'lipid', 'carbohydrate']
            sublista = []
            for macro in list_macro:
                if macro in food:
                    nutrient = f"{normalize(food[macro]['qty'])}" 
                    sublista.append(nutrient)
                else:
                    nutrient = '0'
                    sublista.append(nutrient)
            return sublista


        for food_id in self.list_id:
            for food in food_id: 
                dict_food = {
                    'description': food['description'],
                    'base_qty': food['base_qty'],
                    'kcal': f"{normalize(food['attributes']['energy']['kcal'])}",
                    'kj': f"{normalize(food['attributes']['energy']['kj'])}",
                    'protein': macro_not_exist(food['attributes'])[0],
                    'lipid': macro_not_exist(food['attributes'])[1],
                    'carbohydrate': macro_not_exist(food['attributes'])[2]
                }
                self.list_food.append(dict_food)
        # print(json.dumps(self.list_food, indent=4))
        return self.list_food


    def generate_csv(self):
        list_food = self.taco_food()
        list_local = []
        for registro in list_food:
            list_local.append([registro['description'], registro['base_qty'], registro['kcal'], registro['kj'], registro['protein'], registro['lipid'], registro['carbohydrate']])

        generate_csv = pd.DataFrame(list_local, columns=['Descrição', 'Quantidade(g)', 'Kcal', 'Kj', 'Proteina(g)', 'Gorduras(g)', 'Carboidrato(g)'])

        food_csv = generate_csv.to_excel(f"Cardápio_{self.name_patient}.xlsx", index=False)
        return food_csv

            
if __name__ == "__main__":
    objeto = tacoApi()
    objeto.generate_csv()