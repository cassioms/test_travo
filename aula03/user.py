class User:

    situations = [
        {'lower': 0.0, 'upper': 17.0, 'situation': 'Muito abaixo do peso', 'level': 5},
        {'lower':17.0, 'upper': 18.49, 'situation': 'Abaixo do peso', 'level': 1},
        {'lower': 18.5, 'upper': 24.99, 'situation': 'Peso normal', 'level': 0},
        {'lower': 25.0, 'upper': 29.99, 'situation': 'Acima do peso', 'level': 2},
        {'lower': 30.0, 'upper': 34.99, 'situation': 'Obesidade I', 'level': 3},
        {'lower': 35.0, 'upper': 39.99, 'situation': 'Obesidade II (severa)', 'level': 4},
        {'lower': 40.0, 'upper': 200.0, 'situation': 'Obesidade III (mórbida)', 'level': 6},
    ]


    def __init__(self, user):
        self.id = user['id']
        self.name = user['name']
        self.height = user['height']
        self.weight = user['weight']
        self.update()
    

    def get_imc(self):
        return self.weight / (self.height * self.height)
    

    def get_status(self):
        for situation in User.situations:
            if (self.imc >= situation['lower'] and self.imc < situation['upper']):
                return situation['situation'], situation['level']


    def __repr__(self):
        return f'User[name:{self.name}|height:{self.height}|weight:{self.weight}|imc:{self.imc}|level:{self.level}]'


    def __gt__(self, other):
        return self.level > other.level


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'height': self.height,
            'weight': self.weight,
            'imc': self.imc,
            'situation': self.situation,
            'level': self.level
        }


    def update(self):
        self.imc = self.get_imc()
        self.situation, self.level = self.get_status()
