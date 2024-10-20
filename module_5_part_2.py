import json

class Model:
    atr1 = 5
    atr2 = 5.23
    atr3 = 'Hello'

    def _save(self):
        attributes = dict.fromkeys(list(filter(lambda x: not x.startswith('_'), dir(Model))), vars(self))
        for keys in attributes.keys():
            attributes[keys] = getattr(self, keys)
        with open('file.json', 'w') as f:
            json.dump(attributes, f)

model = Model()
model._save()
