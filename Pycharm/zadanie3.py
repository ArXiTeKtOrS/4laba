def A():
    print("=" * 60)
    # Ввод очков 20 команд
    points = []
    print("Введите очки 20 команд в порядке убывания:")
    for i in range(1, 21):
        while True:
            try:
                p = int(input(f"Очки команды на месте {i}: "))
                # Проверка порядка убывания
                if i > 1 and p > points[-1]:
                    print(f"Ошибка! Очки должны быть меньше или равны {points[-1]}")
                    continue
                points.append(p)
                break
            except ValueError:
                print("Ошибка! Введите целое число.")
    # Преобразуем список в кортеж
    points_tuple = tuple(points)

    print(f"\n Введенная таблица очков:")
    for i, p in enumerate(points_tuple, 1):
        print(f"{i:2}. {p:3} очков")
    # Поиск команды
    while True:
        try:
            n = int(input("\nВведите очки искомой команды (0 для выхода): "))
            if n == 0:
                break
            if n in points_tuple:
                place = points_tuple.index(n) + 1
                print(f"Команда с {n} очками занимает {place} место")

                # Количество команд с такими же очками
                b = points_tuple.count(n)
                if b > 1:
                    print(f"Примечание: {b} команд имеют по {n} очков")
            else:
                print(f"Команда с {n} очками не найдена")
        except ValueError:
            print("Ошибка ввода!")
# Запуск
if __name__ == "__main__":
    A()