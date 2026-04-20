
# encapsulation types and name mangling


# class BankAccount:
#     def __init__(self,name,balance):
#         self._name = name
#         self.__balance = balance

#     @property
#     def balance(self):
#         print(self.__balance)
#     @balance.setter
#     def balance(self,value):
#         self.__balance = value
#         print(self.__balance)
#     @balance.deleter
#     def delete(self):
#         self.__balance = 0
#         print(self.__balance)


# shah = BankAccount("shahala",650)

# print(shah._name)


# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width
    
# r = Rectangle(5,3)
# print(r.area())


# A list is "iterable," but we can turn it into an "iterator"
# fruits = ["apple", "banana", "cherry"]
# bag = iter(fruits)

# print(next(bag))  # apple
# print(next(bag))  # banana
# print(next(bag))  # cherry

# def simple_generator():
#     yield "First"
#     yield "Second"
#     yield "Third"

# # Create the generator
# gen = simple_generator()

# print(next(gen))  # First
# print(next(gen))  # Second


# names = ["ali","john","sara"]
# marks = [85,90,95]

# for name, mark in zip(names, marks):
#     print(name, mark)

def decorator(func):
    def wrapper(nam):
        return nam.upper()
    return wrapper

@decorator
def name(h):
    return h

print(name("shahala"))
