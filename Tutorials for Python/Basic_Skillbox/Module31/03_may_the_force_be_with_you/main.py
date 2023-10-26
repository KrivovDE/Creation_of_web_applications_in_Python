# TODO здесь писать код


import requests
import json

first_req = requests.get('https://swapi.dev/api/starships/10/')
result_dict = dict()

data = json.loads(first_req.text)


print(data['name'])
print(data['max_atmosphering_speed'])
print(data['starship_class'])
print(data['pilots'])
print()

for i_pilots in data['pilots']:
    pilot = json.loads(requests.get(i_pilots).text)
    print(pilot['name'])
    print(pilot['height'])
    print(pilot['mass'])
    planet = json.loads(requests.get(pilot['homeworld']).text)
    print(planet['name'])
    print(pilot['homeworld'])
    print()

result_dict['name'] = data['name']
result_dict['max_atmosphering_speed'] = data['max_atmosphering_speed']
result_dict['starship_class'] = data['starship_class']
result_dict['pilots'] = {json.loads(requests.get(i_pilots).text)['name'] :
                             [json.loads(requests.get(i_pilots).text)['height'],
                                json.loads(requests.get(i_pilots).text)['mass'],
                                json.loads(requests.get(json.loads(requests.get(i_pilots).text)['homeworld']).text)['name'],
                                json.loads(requests.get(i_pilots).text)['homeworld']
                                                                            ]
                         for i_pilots in data['pilots']}

with open('Result_file.txt', 'w', encoding='utf-8') as file:
    json.dump(result_dict, file, indent=4)


