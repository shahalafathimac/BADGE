
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

# def decorator(func):
#     def wrapper(nam):
#         return nam.upper()
#     return wrapper

# @decorator
# def name(h):
#     return h

# print(name("shahala"))


# def greet_decorator(func):
#     def wrapper(value):
#         if isinstance(value, int):
#             return "hello"
#         elif isinstance(value, str):
#             return "hi"
#         else:
#             return "invalid type"
#     return wrapper


# @greet_decorator
# def greet(x):
#     return x


# # Test
# print(greet(10))      # hello
# print(greet("abc"))   # hi
# print(greet(3.5))     # invalid type


# def decorator(func):
#     def wrapper(value):
#         if isinstance(value, int):
#             return "hello"
#         elif isinstance(value, str):
#             return "hi"
#         else:
#             return "invalid type"
#     return wrapper




# @decorator
# def name(x):
#     return x

# print(name("h"))


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("function started")
#         result = func(*args, **kwargs)
#         print("function ended")
#         return result
#     return wrapper


# @decorator
# def name():
#     print("hello")

# name()

# def decorator(func):
#     def wrapper(*args,**kwargs):
#         result = func(*args, **kwargs)
#         return result.upper()
#     return wrapper
        
        

# @decorator
# def name(x):
#     return x

# print(name("shahala"))


# def decorator(func):
#     def wrapper(value):
#         if value%2==0:
#             return "even"
#         else:
#             return "odd"
#     return wrapper


# @decorator
# def predict(value):
#     return value
# print(predict(4))

# def decorator(func):
#     def wrapper(*args,**kwargs):
#         result = func(*args,**kwargs)
#         return "hello "+ result
#     return wrapper

# @decorator
# def name(value):
#     return value

# print(name("shahala"))

# y = 1008
# x = 1008
# print(x is y)

# a ="hello"
# b = "hello"
# print(a is b)

# a = "hello world"
# b = "hello vorld"
# print(a is b)

# a = 10
# print(hash(a))


# def append_to(item, lst=[]):  
#     lst.append(item)
#     return lst

# print(append_to(1) )
# print(append_to(2) )


# x = [[1, 2], [3, 4]]
# y = x.copy()   

# y.append([5, 6])  
# y[0].append(99)
# print(y)
# x.append([3,6])
# print(x)


# import copy

# original = [[1, 2], {'a': [3, 4]}]
# deep = copy.deepcopy(original)

# deep[0].append(99)
# deep[1]['a'].append(99)
# print(deep)
# print(original)


# class Student:
#     def __init__(self,marks):
#         self.marks = marks
#     def __add__(self, other):
#         return self.marks + other.marks
    
# s1 = Student(50)
# s2 = Student(60)

# print(s1+s2)

class Student:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self,other):
        return self.marks + other.marks
    
    def __radd__(self,other):
        return other + self.marks
    
s1 = Student(50)
print(10+s1)



        