class Data:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        '''
        Функция сравнения/получения значения может быть тяжелой.
        Это искусственное замедление является плейсхолдером для некоторой реальной операции (хэш-функции),
        или тяжелой операции сравнения объектов
        '''
        summa = 0
        for i in range(100):
            summa += i
        return self._value + summa - sum(range(100))

    def __str__(self):
        return f"Data: {str(self._value)}"
