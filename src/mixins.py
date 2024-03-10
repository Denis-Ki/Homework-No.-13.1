class MixinInfo:
    '''
    Миксин для вывода информации о созданном объекте
    '''

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        info = 'Создан объект с прараметрами:\n'
        for key, value in self.__dict__.items():
            info += f'{key}: {value}\n'
        return info
