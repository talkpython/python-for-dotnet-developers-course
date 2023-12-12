import abc


class Car(abc.ABC):
    def __init__(self, model_name: str, engine_type: str, cylinders: int, base_price: float):
        self.base_price: float = base_price
        self.cylinders: int = cylinders
        self.engine_type: str = engine_type
        self.model_name: str = model_name

    def drive(self):
        print(f'Car: The {self.model_name} goes vroom!')

    @abc.abstractmethod
    def refuel(self):
        pass

    @property
    def is_electric(self):
        return self.engine_type == 'electric'

    def __str__(self):
        return f'{type(self).__name__}: Model: {self.model_name}, price: ${self.base_price:,.0f}'

    def __repr__(self):
        return self.__str__()
