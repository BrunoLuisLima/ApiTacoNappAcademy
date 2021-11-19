import requests
import json
import pandas as pd


class tacoApi:
    def __init__(self):
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
        for food_id in self.list_id:
            for food in food_id:
                if 'carbohydrate' in food['attributes']:
                    carbohydrate = f"{food['attributes']['carbohydrate']['qty']:.1f}"
                else:
                    carbohydrate = '0'
                dict_food = {
                    'description': food['description'],
                    'base_qty': food['base_qty'],
                    'kcal': f"{food['attributes']['energy']['kcal']:.1f}",
                    'kj': f"{food['attributes']['energy']['kj']:.1f}",
                    'protein': f"{food['attributes']['protein']['qty']:.1f}",
                    'lipid': f"{food['attributes']['lipid']['qty']:.1f}",
                    'carbohydrate': carbohydrate     
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

        generate_csv.to_excel('cardapio.xlsx', index=False)

            
if __name__ == "__main__":
    objeto = tacoApi()
    objeto.generate_csv()