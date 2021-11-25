from random import randint


class Calcular:

    def __init__(self: object, dificulty: int) -> None:
        self.__dificulty: int = dificulty
        self.__value1: int = self._generate_value
        self.__value2: int = self._generate_value
        self.__operation: int = randint(1, 3)
        self.__result: int = self._generate_result

    @property
    def dificulty(self: object) -> int:
        return self.__dificulty

    @property
    def value1(self: object) -> int:
        return self.__value1

    @property
    def value2(self: object)-> int:
        return self.__value2

    @property
    def operation(self: object) -> int:
        return self.__operation

    @property
    def result(self: object) -> int:
        return self.__result

    def __str__(self: object) -> str:
       op: str = ''
       if self.operation == 1:
           op = 'Sum'
       elif self.operation == 2:
           op = 'Subtract'
       elif self.operation == 3:
           op = 'Multiply'
       else:
           op = 'Unknown operation'
       return f'First value: {self.value1} \nSecond Value: {self.value2}' \
              f'\nDificulty: {self.dificulty} \nOperation: {op}'
    @property
    def _generate_value(self:object) -> int:
        pass

    @property
    def _generate_result(self:object)  -> int:
        pass
    
    @property
    def check_result(self: object, response: int) -> bool:
        pass
    @property
    def show_operation(self: object) -> None:
        pass