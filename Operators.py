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


def student(**kwargs):
    print(kwargs)

student(name= "shahala", age= 22)
