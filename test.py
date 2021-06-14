"""
Создать класс MyTime. Атрибуты: hours, minutes, seconds.
Методы:переопределить магические методы сравнения(==, !=, >=, <=, <, >),
сложения, вычитания, умножения на число, вывод на экран.
Перегрузить конструктор на обработку входных параметров вида:
одна строка, три числа, другой объект класса MyTime, и отсутствие входных параметров.
Реализовать нормальное отображение времени(12:65:83 - 13:06:23)
"""

'''
class MyTime:
    def method1(self, time_string: str):
        time_string = time_string.split(":")
        if len(time_string) != 3:
            print("Некоректно введено время")
        else:
            try:
                self.hours = int(time_string[0])
                self.minutes = int(time_string[1])
                self.seconds = int(time_string[2])
            except:
                print("Некоректно введено время")
                
    def method2(self, hours, minutes, seconds):
        self
'''
class MyTime:
    def __init__(self, time_string: str = None, hours=None, minutes=None, seconds=None, t=None):
        try:
            if time_string:
                time_string = time_string.split(":")
                if len(time_string) != 3:
                    print("Некоректно введено время")
                else:
                    try:
                        self.hours = int(time_string[0])
                        self.minutes = int(time_string[1])
                        self.seconds = int(time_string[2])
                    except:
                        print("Некоректно введено время")
        except Exception as ex:
            print(ex)
        if hours:
            self.hours = hours
            if minutes:
                self.minutes = minutes
                if seconds:
                    self.seconds = seconds

        if t:
            self.hours = t.hours
            self.minutes = t.minutes
            self.seconds = t.seconds

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
t1 = MyTime(hours=2, minutes=30, seconds=45)
t2 = MyTime(hours=2, minutes=30, seconds=45)
t3 = MyTime(hours=16, minutes=15, seconds=20)
print(t1 + t3)
print(t1)
print(t3)
print(t3 - t2)
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
