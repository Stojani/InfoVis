import json


dataset = {
    'nodes': [],
    'links': []
}
with open("./dataset/food_groups.json") as ingr_file:
    data = json.load(ingr_file)
    for i in data:
        group = data.get(i)
        for ingr in (group.get('ingredients')):
            dataset['nodes'].append({'id': ingr, 'idgroup': i, 'group': group.get('name')})

#print(dataset)

index=0

tmp = {}

with open("./dataset/meals.json") as meals_file:
    data2 = json.load(meals_file)
    for p in data2:
        meal = data2.get(p)
        l = meal.get('ingredients')
        # compare all ingredients of a meal to link them
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                # put ingredient as source alphabetically 
                if(l[i] < l[j]):
                    if(l[i] in tmp): # ingredient already source
                        t = tmp.get(l[i])
                        if(l[j] in t): # link already existing source-target ---> increment size
                            for index, link in enumerate(dataset['links']):
                                if(link.get('source') == l[i] and link.get('target') == l[j]):
                                    dataset['links'][index]['size'] +=1
                        else:
                            # link doesn't exist ----> create new link in dataset
                            dataset['links'].append({'source': l[i], 'target': l[j], 'id': index, 'size': 1})
                            index += 1
                            tmp.get(l[i]).append(l[j])
                    else:
                        # link doesn't exist ----> create new link in dataset
                        dataset['links'].append({'source': l[i], 'target': l[j], 'id': index, 'size': 1})
                        index += 1
                        tmp[l[i]] = []
                        tmp.get(l[i]).append(l[j])
                else:
                    # l[j] could be source alphabetically
                    if(l[j] in tmp): # ingredient already source
                        t = tmp.get(l[j])
                        if(l[i] in t): # link already existing source-target ---> increment size
                            for index, link in enumerate(dataset['links']):
                                if(link.get('source') == l[j] and link.get('target') == l[i]):
                                    dataset['links'][index]['size'] +=1
                        else:
                            # link doesn't exist ----> create new link in dataset
                            dataset['links'].append({'source': l[j], 'target': l[i], 'id': index, 'size': 1})
                            index += 1
                            tmp.get(l[j]).append(l[i])
                    else: 
                        # link doesn't exist ----> create new link in dataset
                        dataset['links'].append({'source': l[j], 'target': l[i], 'id': index, 'size': 1})
                        index += 1
                        tmp[l[j]] = []
                        tmp.get(l[j]).append(l[i])


with open("./dataset/ingr_comp.json", "w") as write_file:
    json.dump(dataset, write_file)


        
