from task_12_1 import MyTime

if __name__ == '__main__':
    print("ПРОВЕРКА РАБОТЫ!!!!")

    t1 = MyTime(-50, 100, 0)
    print(t1)
    t2 = MyTime(11, 30, 15)
    print(t2)
    t3 = MyTime(15, 20, 30)
    print(t3)
    print(t2 - t3)
    print(t2 * 6)
    print(t2 < t3)
    print(t2 >= t3)
    t4 = MyTime(11, 30, 15)
    print(t2 == t4)
    print(t2 == t3)