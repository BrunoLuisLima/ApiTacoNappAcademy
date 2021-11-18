import requests

class tacoApi:
    def __init__(self, idtaco):
        self.url = requests.get(f"http://localhost:4000/api/v1/food/{idtaco}/")
        self.list_food = []
    

    def taco_food(self):
        for food in self.url.json():
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
        print(self.list_food)
        return self.list_food
    

    # def salve_csv(self):
    #     for 


if __name__ == "__main__":
    objeto = tacoApi(1)
    objeto.taco_food()