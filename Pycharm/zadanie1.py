print("=" * 50)
A = []
print("Введите 10 элементов списка:")

for i in range(10):
    while True:
        try:
            value = float(input(f"Элемент {i+1}: "))
            A.append(value)
            break
        except ValueError:
            print("Ошибка! Введите число.")

print(f"\nИсходный список: {A}")

# индекс максимального элемента
max_index = A.index(max(A))

# Меняем местами первый элемент и максимальный
if max_index != 0:
    A[0], A[max_index] = A[max_index], A[0]

print(f"Преобразованный список: {A}")
print("=" * 50)