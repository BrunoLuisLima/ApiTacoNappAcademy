import requests

id_taco = input("Digite Numero do alimento desejado: ")

response = requests.get(f"http://localhost:4000/api/v1/food/{id_taco}/")


for item in response.json():
    print(f"Descrição: {item['description']}")
    print(f"Proteina: {item['attributes']['protein']['qty']:.2f}g")
    if 'carbohydrate' in item['attributes']:
        print(f"Carboidrato: {item['attributes']['carbohydrate']['qty']:.2f}g")
    print(f"Gorduras: {item['attributes']['lipid']['qty']:.2f}g")
    print(f"Calorias: {item['attributes']['energy']['kcal']:.2f}kcal ({item['attributes']['energy']['kj']:.2f}kj)")

print(response)