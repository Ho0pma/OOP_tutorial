# class Point:
#     color = 'red'
#     circle = 2
#
# print(Point.__dict__)
#
# a = Point()
# print(a.__dict__)
#
# print(type(a))
# print(isinstance(a, Point))
#
# a.color = 'GREEN'
# print(a.__dict__)
#
# setattr(Point, 'new', 1)
# print(Point.__dict__)
#
# print(Point.color)
# print(getattr(Point, 'a', 1))
#
# del Point.new
# print(hasattr(Point, 'new'))
#
# class Point:
#     'Класс для представления координат точек на плоскости'
#     color = 'black'
#
# a = Point()
# b = Point()
#
# a.x = 1
# a.y = 2
# b.x = 45
# b.y = 6
#
# print(Point.__doc__)
# ------------------------------------------------------------------------------------------------ #

# задача 1.3.3 Объявить класс и его переменные
# class DataBase:
#     pk = 1
#     title = "Классы и объекты"
#     author = "Сергей Балакирев"
#     views = 14356
#     comments = 12
# ------------------------------------------------------------------------------------------------ #

# задача 1.3.4 Объявить класс и его переменные
# потом изменить атрибут price и добавить атрибут inflation
# class Goods:
#     title = "Мороженое"
#     weight = 154
#     tp = "Еда"
#     price = 1024
#
# Goods.price = 2048
# setattr(Goods, 'inflation', 100)
# ------------------------------------------------------------------------------------------------ #

# задача 1.3.5 Объявить пустой класс, потом добавить в него атрибуты
# вывести на экран color
# class Car:
#     pass
#
# setattr(Car, 'model', 'Тойота')
# setattr(Car, 'color', 'Розовый')
# setattr(Car, 'number', 'П111УУ77')
#
# print(Car.color)
# ------------------------------------------------------------------------------------------------ #

# задача 1.3.6 Объявить класс и атрибуты
# вывести на экран значение  author
# class Notes:
#     uid = 1005435
#     title = "Шутка"
#     author = "И.С. Бах"
#     pages = 2
#
# print(getattr(Notes, 'author'))
# ------------------------------------------------------------------------------------------------ #

# задача 1.3.7 Объявить класс и атрибуты
# вывести на экран значение атрибута rus_word если такой есть, если нет - False
# class Dictionary:
#     rus = "Питон"
#     eng = "Python"
#
# print(getattr(Dictionary, 'rus_word', False))
# ------------------------------------------------------------------------------------------------ #

# задача 1.3.8 Объявить класс и атрибут total_blogs
# создать эк и его локал свойства
# увеличить значение total_blogs на 1
# создать еще один эк + лок атрибуты + увеличить total_blogs на 1
# class TravelBlog:
#     total_blogs = 0
#
# tb1 = TravelBlog()
# setattr(tb1, 'name', 'Франция')
# setattr(tb1, 'days', 6)
#
# setattr(TravelBlog, 'total_blogs', 1) # или TravelBlog.total_blogs += 1
#
# tb2 = TravelBlog()
# setattr(tb2, 'name', 'Италия')
# setattr(tb2, 'days', 5)
#
# setattr(TravelBlog, 'total_blogs', 2) # или TravelBlog.total_blogs += 1

# второй варик (лучше)
# class TravelBlog:
#     total_blogs = 0
#
#     def __init__(self, name, days):
#         self.name = name,
#         self.days = days,
#         TravelBlog.total_blogs += 1
#
# tb1 = TravelBlog('Франция', 6)
# tb2 = TravelBlog('Италия', 5)
# ------------------------------------------------------------------------------------------------ #

# задача 1.3.9 Объявить класс и атрибуты
# создать эк и добавить лок атрибуты
# удалить из эк color, вывести на экран список лок свойств без значений
# class Figure:
#     type_fig = 'ellipse'
#     color = 'red'
#
# fig1 = Figure()
# fig1.start_pt = 10, 5
# fig1.end_pt = 100, 20
# fig1.color = 'blue'
#
# del fig1.color
# print(*fig1.__dict__.keys())

# ------------------------------------------------------------------------------------------------ #
# задача 1.3.10 Объявить класс и атрибуты
# создать эк, проверить есть ли свойство job. True если есть, False если нет
# class Person:
#     name = 'Сергей Балакирев'
#     job = 'Программист'
#     city = 'Москва'
#
# p1 = Person()
# print(True if p1.__dict__.get('job') else False)
# # еще вариант: print('job' in p1.__dict__)
# ------------------------------------------------------------------------------------------------ #

# class Point:
#     color = 'red'
#     circle = 2
#
#     def set_coords(self):
#         # print('Вызов метода set_coords' + str(self))
#
#
# pt = Point()
# pt.set_coords()
# Point.set_coords(pt)
# ------------------------------------------------------------------------------------------------ #

# class Point:
#     color = 'red'
#     circle = 2
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point()
# pt2 = Point()
# pt.set_coords(1, 2)
# pt2.set_coords(10, 20)
# print(pt.__dict__)
# print(pt2.__dict__)
# ------------------------------------------------------------------------------------------------ #
#
# class Point:
#     color = 'red'
#     circle = 2
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_coords(self):
#         return self.x, self.y
#
#
# pt = Point()
# pt.set_coords(1, 2)
# print(pt.get_coords())
# f = getattr(pt, 'get_coords')
# print(f())

# ------------------------------------------------------------------------------------------------ #
# задача 1.4.1 Объявить класс и с двумя методами open и play
# создать два эк и вызвать методы
# class MediaPlayer:
#     def open(self, file):
#         self.filename = file
#
#     def play(self):
#         return 'Воспроизведение ' + str(self.filename)
#
# media1 = MediaPlayer()
# media2 = MediaPlayer()
# media1.open('filemedia1')
# media2.open('filemedia2')
# print(media1.play())
# print(media2.play())

# ------------------------------------------------------------------------------------------------ #
# задача 1.4.2 Объявить класс и с двумя методами set_data и draw
# атрибутом LIMIT_Y  = [0, 10]
# создать эк в котором передается список. Если число в списке есть в LIMIT_Y вывести.
# class Graph:
#     LIMIT_Y = [0, 10]
#
#     def set_data(self, data):
#         self.data = data
#
#     def draw(self):
#         return [i for i in self.data if i in range(self.LIMIT_Y[0], self.LIMIT_Y[1] + 1)]
#
#     # # второй вариант draw:
#     # def draw(self):
#     #     a, b = self.LIMIT_Y
#     #     return filter(lambda x: a <= x <= b, self.data)
#
# graph_1 = Graph()
# graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
# print(*graph_1.draw())

# ------------------------------------------------------------------------------------------------ #
# задача 1.4.3 создать локальные атрибуты основанные на поступающем списке

# import sys
#
# class StreamData:
#     def create(self, fields, lst_values):
#         if len(fields) != len(lst_values):
#             return False
#
#         for i, key in enumerate(fields):
#             setattr(self, key, lst_values[i])
#
#         return True
#
#
# class StreamReader:
#     FIELDS = ('id', 'title', 'pages')
#
#     def readlines(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
#         sd = StreamData()
#         res = sd.create(self.FIELDS, lst_in)
#         return sd, res
#
# sr = StreamReader()
# data, result = sr.readlines()
# print(data, result)

# ------------------------------------------------------------------------------------------------ #
# задача 1.4.4: нужно написать два метода класса: insert и select.
# insert - должен конвертить полученный список (lst_in) из строк в словарь по образу
# {'id': '1', 'name': 'Сергей', 'old': '35', 'salary': '120000'} и обновлять список lst_data
# select - выводить полученный список в заданном диапазоне

# lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']
#
# class DataBase:
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')
#
#     def insert(self, data):
#         self.lst_data.extend([dict(zip(self.FIELDS, item.split())) for item in data])
#
#     def select(self, a, b):
#         return self.lst_data[a:b + 1]
#
#
#
# db = DataBase()
# print(db.insert(lst_in))
# print(db.select(0, 1))

# ------------------------------------------------------------------------------------------------ #
# задача 1.4.5: написать три метода add / remove / translate
# add - добавляет слова в формате {'tree': ['дерево', ...]} те может быть несколько значений
#

# class Translator:
#     def add(self, eng, rus):
#         if 'tr' not in self.__dict__:  # проверяет есть уже такой словарь (эк)
#             self.tr = {}
#
#         self.tr.setdefault(eng, [])
#         if rus not in self.tr[eng]:
#             self.tr[eng].append(rus)
#         return self.tr
#
#     def remove(self, eng):
#         if eng in self.tr:
#             del self.tr[eng]
#         else:
#             print('nothing to delete')
#
#     def translate(self, eng):
#         if eng in self.tr:
#             return self.tr[eng]
#         else:
#             return 'No words like that'
#
# tr = Translator()
# print(tr.add("tree", "дерево"))
# tr.add("car", "машина")
# tr.add("car", "автомобиль")
# tr.add("leaf", "лист")
# tr.add("river", "река")
# tr.add("go", "идти")
# tr.add("go", "ехать")
# tr.add("go", "ходить")
# tr.add("milk", "молоко")
#
# tr.remove('car')
# print(*tr.translate('go'))

# ------------------------------------------------------------------------------------------------ #
# инициализатор и финализатор
# class Point:
#     color = 'red'
#
#     def __init__(self):
#         print('вызов __init__')
#         self.x = 0
#         self.y = 0
#
# pt = Point()
# print(pt.__dict__)

# ------------------------------------------------------------------------------------------------ #
# Как задавать при создании эк локальные атрибуты через мм __init__?
# class Point:
#     color = 'red'
#
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
#
#     def __del__(self):
#         print('Удаление объекта' + str(self))
#
# pt = Point(10, 20)

# ------------------------------------------------------------------------------------------------ #
# задача: 1.5.1 - Объявить класс, что бы можно было при создании эк создавать ла

# class Money:
#     def __init__(self, money):
#         self.money = money
#
# my_money = Money(100)
# print(my_money.__dict__)

# ------------------------------------------------------------------------------------------------ #
# задача: 1.5.2 - Объявить класс, что бы можно было при создании эк создавать ла
# + чтобы был необязательный аргумент
# создать тысячу объектов с координатами (1, 1), (3, 3), (5, 5), ... и поместить в список

# class Point:
#     def __init__(self, x, y, color='black'):
#         self.x = x
#         self.y = y
#         self.color = color
#
# points = [Point(i, i) for i in range(2000) if i % 2 != 0]
# # второй вариант создания списка
# # points = [Point(c, c) for c in range(1, 2000, 2)]
#
# points[1].color = 'yellow'
# # for i in points:
# #     print(i.x, i.y, i.color)
# # print(len(points))

# ------------------------------------------------------------------------------------------------ #
# задача: 1.5.3 - Объявить 3 класса. Создать 3 эк, с передаваемыми аргументами.
# import random
# class Line:
#     def __init__(self, a, b, c, d):
#         self.sp = a, b
#         self.ep = c, d
#
# class Rect:
#     def __init__(self, a, b, c, d):
#         self.sp = a, b
#         self.ep = c, d
#
# class Ellipse:
#     def __init__(self, a, b, c, d):
#         self.sp = a, b
#         self.ep = c, d
#
# name_classes = ['Line', 'Rect', 'Ellipse']
# r_int = [random.randint(1, 100) for i in range(4)]
# elements = [globals()[random.choice(name_classes)](r_int[0], r_int[1], r_int[2], r_int[3])
#             for _ in range(217)]
#
# for i in elements:
#     if isinstance(i, Line):
#         i.ep = 0, 0
#         i.sp = 0, 0
#     print(i.ep, i.sp)

# ------------------------------------------------------------------------------------------------ #
# второй вар, получше
# import random
#
# class Figure:
#     def __init__(self, a, b, c, d):
#         self.sp = a, b
#         self.ep = c, d
# class Line(Figure):
#     pass
#
# class Rect(Figure):
#     pass
#
# class Ellipse(Figure):
#     pass
#
#
# elements = [random.choice((Line, Rect, Ellipse))(*random.sample(range(10), 4)) for _ in range(217)]
# # elements = [(Line, Rect, Ellipse)[random.randint(0, 2)](1, 2, 3, 4) for _ in range(217)]
#
# for i in elements:
#     if isinstance(i, Line):
#         i.ep = 0, 0
#         i.sp = 0, 0
#     print(i.ep, i.sp)

# ------------------------------------------------------------------------------------------------ #
# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         if not all(map(lambda x: type(x) in (int, float), (self.a, self.b, self.c))):
#             return 1
#         if not all(map(lambda x: x > 0, (self.a, self.b, self.c))):
#             return 1
#         elif self.a + self.b <= self.c or self.a + self.c <= self.b or self.c + self.b <= self.a:
#             return 2
#         else:
#             return 3
#
# a, b, c = map(int, input().split()) # эту строчку не менять
#
# tr = TriangleChecker(a, b, c)
# print(tr.is_triangle())













