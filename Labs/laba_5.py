from abc import ABC, abstractmethod

class Database(ABC): # интерфейс базы данных (Прокси)
    @abstractmethod
    def query(self, sql):
        pass
class RealDatabase(Database):
    def query(self, sql):
        print(f"Executing query: {sql}")

class DatabaseProxy(Database): # прокси с проверкой доступа
    def __init__(self, has_access):
        self._real_database = RealDatabase()
        self._has_access = has_access

    def query(self, sql):
        if self._has_access:
            self._real_database.query(sql)
        else:
            print("Access denied. Query cannot be executed.")

if __name__ == "__main__": # пример использования
    user_db = DatabaseProxy(False)
    admin_db = DatabaseProxy(True)

    user_db.query("SELECT * FROM users")  # Access denied
    admin_db.query("SELECT * FROM users")  # Executing query


class ExternalLogger: # сторонний класс (Адаптер)
    def log_message(self, msg):
        print(f"External log: {msg}")

class Logger: # целевой интерфейс
    def log(self, message):
        pass

class LoggerAdapter(Logger):
    def __init__(self, external_logger):
        self._external_logger = external_logger

    def log(self, message):
        self._external_logger.log_message(message)

if __name__ == "__main__":
    external_logger = ExternalLogger()
    logger = LoggerAdapter(external_logger)

    logger.log("This is a test message.")




class Device(ABC): # интерфейс устройства (Мост)
    @abstractmethod
    def print(self, data):
        pass

class Monitor(Device): # конкретные устройства
    def print(self, data):
        print(f"Displaying on monitor: {data}")

class Printer(Device):
    def print(self, data):
        print(f"Printing to paper: {data}")


class Output(ABC): # абстракция
    def __init__(self, device: Device):
        self._device = device

    @abstractmethod
    def render(self, data):
        pass

class TextOutput(Output): # расширенная абстракция
    def render(self, data):
        self._device.print(f"Text: {data}")

class ImageOutput(Output):
    def render(self, data):
        self._device.print(f"Image: [Binary data: {data}]")


if __name__ == "__main__":
    monitor = Monitor()
    printer = Printer()

    text_on_monitor = TextOutput(monitor)
    text_on_printer = TextOutput(printer)

    text_on_monitor.render("Hello, world!")
    text_on_printer.render("Hello, world!")

    image_on_monitor = ImageOutput(monitor)
    image_on_monitor.render("101010101")  # Displaying on monitor: Image: [Binary data: 101010101]

