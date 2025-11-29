
class ClientSideError(Exception):
    """
    Пользовательское исключение для ошибок на стороне клиента.
    """
    def __init__(self, message="Ошибка на стороне клиента. Попробуйте снова."):
        self.message = message
        super().__init__(self.message)

class ServerSideError(Exception):
    """
    Пользовательское исключение для ошибок на стороне сервера.
    """
    def __init__(self, message="Ошибка на стороне сервера. Простите, но мы не можем ничего сделать."):
        self.message = message
        super().__init__(self.message)

class SillyException(Exception):
        def __init__(self, message="Непонятная ошибка, завершаю работу"):
            self.message = message
            super().__init__(self.message)

class IncorrectInput(Exception):
    def __init__(self, message = 'Неверный ввод. Попробуй снова.'):
        self.message = message
        super().__init__(self.message)

class MyValueError(Exception):
        def __init__(self, message='Введено неправильное значение. Попробуйте снова'):
            self.message = message
            super().__init__(self.message)

class TemporaryUnavailable(Exception):
    def __init__(self, message = 'Функция в разработке. Проверьте GitHub репозиторий на наличие обновлений'):
        self.message = message
        super().__init__(self.message)

class NotFound(Exception):
    def __init__(self, message = 'Ничего не найдено. Пожалуйста, проверьте ввод'):
        self.message = message
        super().__init__(self.message)
