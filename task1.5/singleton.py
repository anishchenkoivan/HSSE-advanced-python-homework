class NewBasedSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(NewBasedSingleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value


inst1 = NewBasedSingleton(1)
inst2 = NewBasedSingleton(2)
assert inst1 is inst2


def singleton(cls):
    instance = None
    def _singleton(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance
    return _singleton


@singleton
class DecoratorBasedSingleton:
    def __init__(self, value):
        self.value = value


inst1 = DecoratorBasedSingleton(1)
inst2 = DecoratorBasedSingleton(2)
assert inst1 is inst2


class MetaSingleton(type):
    _instance = None
    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instance


class MetaclassBasedSingleton(metaclass=MetaSingleton):
    def __init__(self, value):
        self.value = value


inst1 = MetaclassBasedSingleton(1)
inst2 = MetaclassBasedSingleton(2)
assert inst1 is inst2
