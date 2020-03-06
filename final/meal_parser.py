import json


dataset = {
    'nodes': [],
    'links': []
}
with open("./dataset/ingredients.json") as ingr_file:
    data = json.load(ingr_file)
    for i in data:
        dataset['nodes'].append({'id': i, 'group': 'ingr'})

index=0

with open("./dataset/meals.json") as meals_file:
    data2 = json.load(meals_file)
    for p in data2:
        meal = data2.get(p)
        dataset['nodes'].append({'id': meal.get('name'), 'area': meal.get('area'), 'category': meal.get('category'), 'group': 'meal'})
        for j in meal.get('ingredients'):
            dataset['links'].append({'source': meal.get('name'), 'target': j, 'id': index})
            index += 1

with open("./dataset/meals_graph.json", "w") as write_file:
    json.dump(dataset, write_file)


        
