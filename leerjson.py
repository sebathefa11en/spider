import json

with open('out.json') as file:
    data = json.load(file)

    for client in range(3, 19):
        data1 = str(data[client]['pregunta'])
        data2 = data1.encode('utf-8')
        print(data1)
        print('')


