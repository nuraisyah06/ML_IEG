import json

try:
    with open('fruitdictionary.json') as filehandler:
        data = json.load(filehandler)
    for product in data:
        print(product['product'])
        print(quantity['quantity'])
        print(price['price'])
except:
    print("Error")