import requests
import json
import pandas as pd


class ApiExtracty:
    def __init__(self, id_main, pacient):
        self.name_pacient = pacient
        self.list_id = id_main
        self.list_food = []

    def normalize(self, attributes):
        if type(attributes) == float:
            new_value = f"{attributes:.1f}"
        else:
            new_value = attributes
        return new_value.replace('.', ',')
    
    def food_not_exist(self, food):
        list_macro = ['protein', 'lipid', 'carbohydrate']
        sublista = []
        for macro in list_macro:
            if macro in food:
                nutrient = f"{self.normalize(food[macro]['qty'])}" 
                sublista.append(nutrient)
            else:
                nutrient = '0'
                sublista.append(nutrient)
        return sublista

    def taco_food(self):
        list_taco = []
        for id_taco in self.list_id:
            url = requests.get(f"http://localhost:4000/api/v1/food/{id_taco}/")
            list_taco.append(url.json())
            
        for food_id in list_taco:
            for food in food_id: 
                dict_food = {
                    'description': food['description'],
                    'base_qty': food['base_qty'],
                    'kcal': f"{self.normalize(food['attributes']['energy']['kcal'])}",
                    'kj': f"{self.normalize(food['attributes']['energy']['kj'])}",
                    'protein': self.food_not_exist(food['attributes'])[0],
                    'lipid': self.food_not_exist(food['attributes'])[1],
                    'carbohydrate': self.food_not_exist(food['attributes'])[2]
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

        food_csv = generate_csv.to_excel(f"Cardápio_{self.name_pacient}.xlsx", index=False)
        return food_csv

# if __name__ == "__main__":
#     objeto = ApiExtracty()
#     objeto.generate_csv()