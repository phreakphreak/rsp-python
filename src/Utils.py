import json




def find(pred, iterable):
    for element in iterable:
        if pred(element):
            return element
    return None


def readFile(filename="src/data.json"):
    with open(filename, 'r') as f:
        data = json.load(f)
        return data


def writeFile(data, filename="src/data.json"):
    with open(filename, 'w') as f:
        json.dump(data, f)

