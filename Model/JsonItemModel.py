class JsonItemModel:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_object(self):
        return '"' + self.name + '": "' + self.value + '"'
