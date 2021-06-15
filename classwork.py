import math
from time import sleep
# ---------Polimorph-------------

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'My name is {self.name}. I am {self.age}.')

#     def voice(self):
#         print('Wof wof')


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'My name is {self.name}. I am {self.age}.')

#     def voice(self):
#         print('Meow')


# cat1 = Cat('Kitty', 2)
# dog1 = Dog('Rex', 4)

# cat1.voice()
# cat1.info()

# dog1.voice()
# dog1.info()

# --------Inheritance---------

# class A:

#     def m1(self):
#         return '(From A m1)'

#     def m2(self):
#         return '(From A m2)'


# class B:

#     def m3(self):
#         return '(From B m3)'

#     def m2(self):
#         return '(From B m2)'


# class C(B, A):
#     pass


# c = C()

# print(c.m1(), c.m2(), c.m3())


# class Door:

#     color = 'black'
#     material = 'wood'

#     def __init__(self, number, status='close'):
#         self.number = number
#         self.status = status

#     def open(self):
#         self.status = 'open'

#     def close(self):
#         self.status = 'close'


# class SecuredDoor(Door):
#     material = 'steel'

#     def __init__(self, number, status, locked=True):
#         # super().__init__(number, status)
#         Door.__init__(self, number, status)
#         self.locked = locked

#     def open(self):
#         if not self.locked:
#             self.status = 'open'


# door1 = Door(66, 'closed')

# print(door1.status)
# # print(door1.color)

# door2 = SecuredDoor(33, 'closed', )

# # print(door2.status)
# # print(door2.color)

# print(door1.__dict__)
# print(door2.__dict__)
# print(door1.__dir__())
# print()
# print(door2.__dir__())
# print(door2)


# class Shape:

#     color = 'red'

#     def __init__(self, name) -> None:
#         self.name = name

#     def area(self):
#         pass

#     def desc(self):
#         return 'Unknown figure!'

#     def __str__(self) -> str:
#         return 'Instance of ' + self.name

#     def __repr__(self) -> str:
#         return 'Figure: ' + self.name

#     def __del__(self):
#         print('Figure: ' + self.name + 'was remowed!')


# class Circle(Shape):

#     def __init__(self, radius) -> None:
#         super().__init__('Circle')
#         self.radius = radius

#     @classmethod
#     def fig(cls, color: str):
#         cls.color = color
#         return 'Class Method' + cls.color

#     @staticmethod
#     def func(x):
#         return 'Static Method! ' * x

#     def desc(self):
#         return "This is a " + self.name

#     def area(self):
#         return math.pi * self.radius ** 2


# circle = Circle(10)

# print(circle.area())

# print(circle.__repr__())

# print(circle.__class__)
# print(Circle.__class__)
# # sleep(5)
# print(type(circle) == '__main__.Circle')
# print(circle.__class__ == '__main__.Circle')
# print(isinstance(circle, Shape))

# print(circle.func(5))
# print(circle.fig('green'))
# class Singletone:
#     obj = None

#     def __new__(cls, *arg, **kwarg):
#         if cls.obj is None:
#             cls.obj = object.__new__(cls, *arg, **kwarg)
#         return cls.obj

#     def __init__(self) -> None:
#         print('Init', type(self))


# s1 = Singletone()
# s2 = Singletone()

# print(id(s1), id(s2))


# class MyCl:
#     cm = []
#     ci = 'cl_inm'

#     def __init__(self) -> None:
#         self.im = []
#         self.ii = 'instanse_inm'


# a = MyCl()

# print(a.cm, a.ci, a.im, a.ii)

# b = MyCl()
# b.cm.append(11)
# b.ci = 'new_cl_inm'
# b.im.append(22)
# b.ii = 'new_ii'
# print(a.cm, a.ci, a.im, a.ii)
# print(b.cm, b.ci, b.im, b.ii)


# c = MyCl()
# c.im.append(33)
# c.ii = 'C_new_ii'
# print(c.cm, c.ci, c.im, c.ii)
