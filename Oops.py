
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

# class Student:
#     def __init__(self, marks):
#         self.marks = marks

#     def __add__(self,other):
#         return self.marks + other.marks
    
#     def __radd__(self,other):
#         return other + self.marks
    
# s1 = Student(50)
# print(10+s1)


# if (n :=10)>5:
#     print(n)

# age = 20
# store = "adult" if age >= 18 else "minor"
# print(store)


# items = [1,2,3]
# target = 4
# for item in items:
#     if item == target:
#         print("Found!")
#         break
# else:
#     print("Not found!")


# names = ['apple','banana','orange']
# for keys, values in enumerate(names):
#     print(keys, values)

# names = ['apple','orange','banana']
# refers = ['a','b','c']
# num = zip(names, refers)
# print(list(num))

# from itertools import zip_longest
# lis = [1,2,3,4]
# lis1 = [6,7,2]
# result = list(zip_longest(lis,lis1))
# print(result)

# def outer():
#     x = 10

#     def inner():
#         print(x)

#     return inner
# f =outer()
# f()


# class Student:
#     count =0 

#     def __init__(self):
#         Student.count+=1

#         @classmethod
#         def get_count(cls):
#             return cls.count
        
# print(Student.get_count())


# x = 10
# print(x)
# del x
# print(x)


# names = ["ali", "john", "meera"]

# gen = (name.upper() for name in names)

# for name in gen:
#     print(name)

# import copy

# original = {
#     "name": "Ali",
#     "marks": [80, 90]
# }

# shallow = copy.copy(original)

# # Modify nested list
# shallow["marks"][0] = 100

# print("Original:", original)
# print("Shallow:", shallow)
# shallow["name"] = "shahala"
# print("shallow", shallow)
# print(original)

# a = "shahala"
# def name(s):
#     res = {}
#     for i in s:
#         res[i]=res.get(i,0)+1
#     return res

# print(name(a))

# result = {ch: a.count(ch) for ch in a}
# print(result)

# s ="inshad"
# rev = ""
# i = len(s)-1

# while i>=0:
#     rev += s[i]
#     i-=1

# print(rev)

# s = "inshad"
# b = s[::-1]
# print(b)

# s = "hello"
# rev =""
# for ch in s:
#     rev = ch + rev
# print(rev)


# s = "madam"
# print(s == s[::-1])

# print(s =="".join(reversed(s)))
# def name(s):
#     freq ={}
#     for i in s:
#         freq[i] = freq.get(i,0)+1
#     return freq
# print(name(s))

# s = "programming"

# freq = {}

# # Count frequency
# for ch in s:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1
# print()


# s1 = "listen"
# s2 = "silent"

# print(sorted(s1) == sorted(s2))

# def factorial(n):
#     if n == 0 or n == 1:   
#         return 1
#     return n * factorial(n - 1)

# print(factorial(5)) 




# class Parent:
#     def greet(self):
#         print("Hello from Parent")

# class Child(Parent):
#     def welcome(self):
#         print("Hello from Child")

# c = Child()
# c.greet()
# c.welcome()


# class Student:
#     school = "ABC School"  

#     def __init__(self, name):
#         self.name = name

# s1 = Student("Ali")
# s2 = Student("Asha")

# print(s1.school)   
# print(s2.school)   
# print(s1.name)
# print(s2.name)
# Student.school= "def school"
# print(s1.school)

# class Parent:
#     def show(self):
#         print("Parent class")

# class Child(Parent):
#     def display(self):
#         print("Child class")

# c = Child()
# c.show()
# c.display()



# class Father():
#     def saleem(self):
#         print("hero")

# class Mother():
#     def rahiyanath(self):
#         print("heroin")

# class Daughter(Father,Mother):
#     def shahala(self):
#         print("queen")

# c = Daughter()
# c.saleem()
# c.rahiyanath()
# c.shahala()


# class Father():
#     def saleem(self):
#         print("hero")

# class Mother(Father):
#     def Rahiyanath(self):
#         print("heroin")

# class Daughter(Mother):
#     def shahala(self):
#         print("queen")

# c = Daughter()
# c.shahala()
# c.Rahiyanath()
# c.saleem()
# d = Mother()
# d.Rahiyanath()
# d.saleem()


# class Father():
#     def saleem(self):
#         print("hero")

# class Daughter(Father):
#     def shahala(self):
#         print("queen")

# class Son(Father):
#     def shahal(self):
#         print("king")

# c = Son()
# c.saleem()
# c.shahal()
# d = Daughter()
# d.shahala()
# d.saleem()


# class Father():
#     def saleem(self):
#         print("hero")

# class Mother(Father):
#     def mother(self):
#         print("heroin")

# class Daughter(Father):
#     def shahala(self):
#         print("queen")

# class Son(Mother, Daughter):
#     def shahal(self):
#         print("king")

# c = Son()
# c.shahal()
# c.mother()
# c.shahala()
# d =Daughter()
# d.shahala()
# d.saleem()


# class target():
#     def add(self,a,b,c=0):
#         return a+b+c
    
# c =target()
# print(c.add(2,4))
# print(c.add(2,6,5))


# class Animal():
#     def sound(self):
#         print("same sound")

# class Cat(Animal):
#     def sound(self):
#         print("meow")

# class Dog(Animal):
#     def sound(self):
#         print("boww")

# a = Animal()
# c = Cat()
# d = Dog()
# c.sound()



# class Dog(): 
#     def speak(self):
#         print("bow")

# class Cat():
#     def speak(self):
#         print("meow")

# def name(a):
#     a.speak() 

# d =Dog()
# c = Cat()

# name(d)
# name(c)


# class Student():
#     def __init__(self):
#         self.name = "shahala"

# c = Student()
# print(c.name)
# c.name ="shahal"
# print(c.name)


# class Student():
#     def __init__(self):
#         self.name ="shahala"

# c = Student()
# print(c.name)
# c.name = "shahal"
# print(c.name)



# class Parent():
#     def __init__(self):
#         self._salary = 50000

# class Child(Parent):
#     def show(self):
#         print(self._salary)

# c = Child()
# c.show()
# c.salary = 20000
# print(c.salary)


# class Bank():
#     def __init__(self):
#         self.__balance = 10000
#     @property
#     def balance(self):
#         return self.__balance

# c = Bank()
# print(c.balance)


# class Bank():
#     def __init__(self):
#         self.__balance = 2000

#     def bank_balance(self):
#         print(self.__balance)

# c = Bank()
# print(c._Bank__balance)














