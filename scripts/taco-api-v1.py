import requests
import json


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
                    carbohydrate = food['attributes']['carbohydrate']['qty']
                else:
                    carbohydrate = '0'
                dict_food = {
                    'description': food['description'],
                    'base_qty': food['base_qty'],
                    'protein': food['attributes']['protein']['qty'],
                    'carbohydrate': carbohydrate,
                    'lipid': food['attributes']['lipid']['qty'],
                    'kcal': food['attributes']['energy']['kcal'],
                    'kj': food['attributes']['energy']['kj']
                }
                self.list_food.append(dict_food)
        print(json.dumps(self.list_food, indent=4))
        return self.list_food


if __name__ == "__main__":
    objeto = tacoApi()
    objeto.taco_food()