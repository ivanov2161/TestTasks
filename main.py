# coding=utf-8

# TASK 1
# Плюс исходной функции - её краткая запись
def isEven(value):
    return value%2==0  # Минус - запись не отвечает требованиям PEP 8


# Плюс переделанной функции - в явном указании выходных данных функции
def is_even(value):
    if value % 2 == 0:
        return True
    else:
        return False


# TASK 2 - к сожалению придумал только один способ реализации
class Queue:
    '''
    param maxlen: Determines the maximum queue length
    '''
    def __init__(self, maxlen):
        self.maxlen = maxlen
        self.data = list(range(0, self.maxlen))
        self.index = 0

    def add(self, value):
        if self.index >= self.maxlen:
            self.index = 0
        self.data[self.index] = value
        self.index += 1

    def get(self):
        if len(self.data) == 0:
            return []
        value = self.data[0]
        self.data.pop(0)
        return value

    def __str__(self):
        return str(self.data)


# TASK 3
def quicksort(array):  # Данный метод сортировки узнал из книги "Грокаем алгоритмы", сложность алгоритма O(n log n) -
    # что по уверению автора является одним из самых быстрых существующих алгоритмов сортировки.
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
