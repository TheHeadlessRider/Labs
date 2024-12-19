from abc import ABC, abstractmethod

class SortingStrategy(ABC): # интерфейс стратегии
    @abstractmethod
    def sort(self, array):
        pass

class BubbleSortStrategy(SortingStrategy): # пузырьковая сортировка
    def sort(self, array):
        print("Sorting using Bubble Sort")
        n = len(array)
        for i in range(n):
            for j in range(0, n-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]

class QuickSortStrategy(SortingStrategy):
    def sort(self, array):
        print("Sorting using Quick Sort")
        self._quick_sort(array, 0, len(array) - 1)

    def _quick_sort(self, array, low, high):
        if low < high:
            pi = self._partition(array, low, high)
            self._quick_sort(array, low, pi-1)
            self._quick_sort(array, pi+1, high)

    def _partition(self, array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i+1], array[high] = array[high], array[i+1]
        return i+1

class Sorter: # контекст
    def __init__(self, strategy: SortingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self._strategy = strategy

    def sort_array(self, array):
        self._strategy.sort(array)


if __name__ == "__main__": # пример использования
    sorter = Sorter(BubbleSortStrategy())
    array1 = [5, 3, 8, 4, 2]
    sorter.sort_array(array1)
    print("Sorted array:", array1)

    sorter.set_strategy(QuickSortStrategy())
    array2 = [5, 3, 8, 4, 2]
    sorter.sort_array(array2)
    print("Sorted array:", array2)


class Handler(ABC): # интерфейс обработчика
    def __init__(self, next_handler=None):
        self._next_handler = next_handler

    @abstractmethod
    def handle_request(self, request):
        if self._next_handler:
            return self._next_handler.handle_request(request)
        return None

class ConcreteHandlerA(Handler): # конкретный обработчик A
    def handle_request(self, request):
        if request == "TYPE_A":
            return "Handler A processed the request."
        return super().handle_request(request)

class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == "TYPE_B":
            return "Handler B processed the request."
        return super().handle_request(request)


if __name__ == "__main__": # пример использования
    handler_chain = ConcreteHandlerA(ConcreteHandlerB())

    requests = ["TYPE_A", "TYPE_B", "TYPE_C"]
    for req in requests:
        result = handler_chain.handle_request(req)
        if result:
            print(f"Request '{req}' handled: {result}")
        else:
            print(f"Request '{req}' was not handled.")



class Iterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def has_next(self):
        return self._index < len(self._collection)

    def next(self):
        if self.has_next():
            item = self._collection[self._index]
            self._index += 1
            return item
        raise StopIteration

class IterableCollection: # коллекция с итератором
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def get_iterator(self):
        return Iterator(self._items)

if __name__ == "__main__": # пример использования
    collection = IterableCollection()
    collection.add_item("Item 1")
    collection.add_item("Item 2")
    collection.add_item("Item 3")

    iterator = collection.get_iterator()
    while iterator.has_next():
        print(iterator.next())
