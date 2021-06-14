"""
Создать класс MyTime. Атрибуты: hours, minutes, seconds.
Методы:переопределить магические методы сравнения(==, !=, >=, <=, <, >),
сложения, вычитания, умножения на число, вывод на экран.
Перегрузить конструктор на обработку входных параметров вида:
одна строка, три числа, другой объект класса MyTime, и отсутствие входных параметров.
Реализовать нормальное отображение времени(12:65:83 - 13:06:23)
"""


class MyTime:
    __hours: int
    __minutes: int
    __seconds: int

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, hours):
        if 0 > hours > 24:
            print("Количетво часов должно быть в диапазоне от 0 до 24")
        else:
            self.__hours = hours

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, minutes):
        if 0 <= minutes < 60:
            self.__minutes = minutes
        else:
            self.__hours += minutes//60
            self.__minutes = minutes%60

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, seconds):
        if 0 <= seconds < 60:
            self.__seconds = seconds
        else:
            self.__minutes += seconds//60
            self.__seconds = seconds%60

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __add__(self, other):
        return MyTime(self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds)

    def __sub__(self, other):
        return MyTime(self.hours - other.hours, self.minutes - other.minutes, self.seconds - other.seconds)

    def __mul__(self, other):
        return MyTime(self.hours * other, self.minutes * other, self.seconds * other)

    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds

    def __ne__(self, other):
        return self.hours != other.hours and self.minutes != other.minutes and self.seconds != other.seconds

    def __lt__(self, other):
        return self.hours < other.hours and self.minutes < other.minutes and self.seconds < other.seconds

    def __gt__(self, other):
        return self.hours > other.hours and self.minutes > other.minutes and self.seconds > other.seconds

    def __le__(self, other):
        return self.hours <= other.hours and self.minutes <= other.minutes and self.seconds <= other.seconds

    def __ge__(self, other):
        return self.hours >= other.hours and self.minutes >= other.minutes and self.seconds >= other.seconds

    def __str__(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"


print("ПРОВЕРКА РАБОТЫ!!!!")
t1 = MyTime(2, 30, 45)
t2 = MyTime(2, 30, 45)
t3 = MyTime(16, 15, 20)
print(t1 + t3)
print(t1)
print(t3)
print(t3 - t2)
print(t1)
print(t1 * 2)
if t1 == t2:
    print(True)
else:
    print(False)

'''
if t2 >t3:
    print(True)
else:
    print(False)
'''

print("|"*100)
