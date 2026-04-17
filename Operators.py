# a = [1,2]
# b = a
# print(a is b)


# marks = 75
# if marks>=90:
#     print('A')
# elif marks>=80:
#     print("B")
# elif marks>=70:
#     print("c")
# else:
#     print("D")


# day = 4
# match day:
#     case 1:
#         print("monday")
#     case 2:
#         print("tuesday")
#     case 3:
#         print("wednesday")
#     case 4:
#         print("thursday")
#     case _:
#         print("invalid")

# age = 20
# if age >= 18:
#     if age >= 60:
#         print("Senior")
#     else:
#         print("Adult")

# for i in range(1,5):
#     print(i)



# for i in range(5):
#     if i == 3:
#         break
#     print(i)


# for i in range(5):
#     pass


# for i in range(1,3):
#     print(i)
# else:
#     print("done")

# for i in range(2):
#     for j in range(2):
#         for k in range(2):
#             print(i, j, k)

# i=0
# while i<5:
#     print(i)
#     i+=1


# i = 1

# while True:
#     print(i)
#     i += 1

#     if i > 5:
#         break


# name = input("eneter your name:")
# print(name)

# age = int(input("eneter your age:"))
# print(age+5)

# print("hello","name", end="-")
# print("world")

# print("A","B","C", sep=".")

# print("hello\nworld")

# for i in range(5,11,2):
#     print(i)


# for i in range(5,1,-1):
#     print(i)

# names = ["A","B","C"]

# for i, name in enumerate(names):
#     print(i, name)

# names = ["A","B","C"]

# for i, name in enumerate(names, start=1):
#     print(i, name)

# nums = [10,20,30,40]
# nums.remove(20)
# nums.pop(1)
# print(nums)

# food = 'pizza'
# food.replace('z','s')
# print(food)

# x = [1,2,3,4,5]
# for i in x:
#     if i == 3:
#         x.remove(i)
# print(x)


# fruits = ['apple','banana','mango','kiwi','grape']
# for f in fruits:
#     if 'a' in f:
#         fruits.remove(f)

# print(fruits)

# x = 0
# for i in range(4):
#     if i % 2 == 0:
#         x+=i
# print(x)

# nums = [1,2,3,4,5,5,4,3]
# squares = [i*2 for i in nums]
# print(squares)

# dic = {i for i in nums}
# print(dic)

# comp = {i : i+1 for i in nums }
# print(comp)

# gen = (x*2 for x in nums)
# print (list(gen))


# matrix = [[1, 2, 3], [4, 5, 6]]

# flat = []
# for row in matrix:
#     for num in row:
#         flat.append(num)
# print(flat)

# matrix = [[1, 2, 3], [4, 5, 6]]

# flat = [num for row in matrix for num in row]

# print(flat)


# total = lambda a,b:a+b
# print(total(3,5))

# def w(name ="guest"):
#     print("hello", name)
# w("shahala")


# def key(name,age):
#     print(name,age)

# key(name="shahala",age=22)

# def val(name,age):
#     print(f"my name is {name} and my age is {age}" )
# val("shahala",22)

# def H(*args):
#     print(sum(args))
# H(1,2,3,4)

# def show(*names):
#     for n in names:
#         print(n)

# show("Ali", "Fathima", "John")


# def student(**kwargs):
#     print(kwargs)

# student(name= "shahala", age= 22)


# class Math:
#     @staticmethod
#     def add(a,b):
#         return a+b
# print(Math.add(3,5))

# class Student:
#     school = "ABC school"

#     @classmethod
#     def get_school(cls):
#         return cls.school
    
# print(Student.get_school())

# class person:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name
    
# p = person("fathima")
# print(p.name)


# x = 10
# y = x

# print(id(x))
# print(id(y))

# a = b = [1, 2, 3]

# print(id(a))
# print(id(b))

# x = "123"
# y = int(x)
# print(type(y))

# x = 10
# y = str(x)
# print(type(y))

# num = 3

# if num%2 ==0:
#     print("even")
# else:
#     print("odd")

# num = 2
# result = "even" if num%2==0 else "odd"
# print(result)


# num = 2

# match num:
#     case 1:
#         print("One")
#     case 2:
#         print("Two")
#     case _:
#         print("Other")

# day = 'sat'
# match day:
#     case 'mon' | 'tue' | 'wed' | 'thu' | 'fri':
#         print("weekday")
#     case 'sat' | 'sun':
#         print('weekend')
#     case _:
#         print('invalid day')

# num = 15

# match num:
#     case n if n > 10:
#         print("Greater than 10")
#     case n if n > 5:
#         print("Greater than 5")
#     case _:
#         print("Small number")

# numbers = [1,2,3,4,5]
# for n in numbers:
#     print(n)

# i = 0

# while i < 5:
#     print(i)
#     i +=1

# for n in range(1,11):
#     print(n)


lis = [1,2,2,3,3,3,4]
# print(list(set(lis)))

# unique = []
# for n in lis:
#     if n not in unique:
#         unique.append(n)
# print(unique)

# lis =[1,2,3]
# lis.append(4)
# print(lis)

# lis = [1,2,3]
# lis.extend([4,5])
# print(lis)

# lis = [x**2 for x in range(1,11)]
# print(lis)

# lis = [2,4,5,1,6]
# u =lis[::-1]
# print(u)

# set1 = {1,2,3,4}
# set2 = {4,5,6}
# set3 = set1 & set2
# print(set3)
# set3 =set1.intersection(set2)
# print(set3)

# dic1 ={
#     "name":"shahala",
#     "age":22
# }
# dic2 ={
#     "place":"palazhi",

# }
# dic1.update(dic2)
# print(dic1)

# dic ={"a":1,"b":2}
# dic.setdefault("c",3)
# print(dic)

# text = "shahala"
# if text == text[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")


# text = "shahala"
# print(text[::-1])

# text = "my name is shahala"
# words = text.split()
# reversed_words = [word[::-1] for word in words]
# result = " ".join(reversed_words)
# print(result)







