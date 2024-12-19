# Singleton
class Singleton:
    _instance = None  # хранит единственный экземпляр класса

    def __new__(cls, *args, **kwargs):
        if not cls._instance:  # проверка экземпляра
            cls._instance = super().__new__(cls, *args, **kwargs)  # создание экземпляра
        return cls._instance

# проверка Singleton
singleton1, singleton2 = Singleton(), Singleton()
print(f"Singleton works: {singleton1 is singleton2}")  # проверка, что оба объекта ссылаются на один экземпляр

# Factory Method
class Logger:
    def log(self, message): pass

class FileLogger(Logger):
    def log(self, message): print(f"File log: {message}")  # логирование в файл

class ConsoleLogger(Logger):
    def log(self, message): print(f"Console log: {message}")

class LoggerFactory:
    def create_logger(self): raise NotImplementedError  # метод создания логгера

class FileLoggerFactory(LoggerFactory):
    def create_logger(self): return FileLogger()  # создаем объект FileLogger

class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self): return ConsoleLogger()

# Проверка Factory Method
file_logger = FileLoggerFactory().create_logger()  # создаем файловый логгер
console_logger = ConsoleLoggerFactory().create_logger()
file_logger.log("Message for file")  # логируем сообщение в файл
console_logger.log("Message for console")

# Abstract Factory
class Button:
    def render(self): pass  # интерфейс для кнопок

class Checkbox:
    def render(self): pass

class WindowsButton(Button):
    def render(self): return "Windows Button"  # реализация кнопки для Windows

class MacButton(Button):
    def render(self): return "Mac Button"

class WindowsCheckbox(Checkbox):
    def render(self): return "Windows Checkbox"

class MacCheckbox(Checkbox):
    def render(self): return "Mac Checkbox"

class GUIFactory:
    def create_button(self): raise NotImplementedError  # метод создания кнопки
    def create_checkbox(self): raise NotImplementedError

class WindowsFactory(GUIFactory):
    def create_button(self): return WindowsButton()  # создаем Windows-кнопку
    def create_checkbox(self): return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self): return MacButton()  # создаем Mac-кнопку
    def create_checkbox(self): return MacCheckbox()

# Проверка Abstract Factory
windows_ui = WindowsFactory()  # фабрика для Windows
mac_ui = MacFactory()
print(windows_ui.create_button().render(), windows_ui.create_checkbox().render())  # рендер элементов Windows
print(mac_ui.create_button().render(), mac_ui.create_checkbox().render())

# Builder
class Pizza:
    def __init__(self): self.dough = self.sauce = self.topping = None  # инициализируем атрибуты пиццы
    def __str__(self): return f"Pizza(dough={self.dough}, sauce={self.sauce}, topping={self.topping})"  # отображение пиццы

class PizzaBuilder:
    def __init__(self): self.pizza = Pizza()  # инициализируем объект пиццы
    def set_dough(self, dough): self.pizza.dough = dough; return self  # добавляем тесто
    def set_sauce(self, sauce): self.pizza.sauce = sauce; return self
    def set_topping(self, topping): self.pizza.topping = topping; return self
    def build(self): return self.pizza

# Проверка Builder
pizza = PizzaBuilder().set_dough("thin").set_sauce("tomato").set_topping("cheese").build()  # создаём пиццу
print(pizza)  # выводим параметры пиццы



