def sum_otr(numbers):
    """Вычисляем сумму отрицательных элементов"""
    return sum(x for x in numbers if x < 0)

def max_min_index(numbers):
    """Находим индексы максимального и минимального элементов"""
    max_ind = numbers.index(max(numbers))
    min_ind = numbers.index(min(numbers))
    return max_ind, min_ind

def product_between(numbers, ind1, ind2):
    """Вычисляем произведение элементов между двумя индексами"""
    start = min(ind1, ind2)
    end = max(ind1, ind2)

    if end - start <= 1:
        return None

    product = 1
    for i in range(start + 1, end):
        product *= numbers[i]
    return product
def main():
    print("Введите вещественные числа через пробел:")
    numbers = [float(x) for x in input().split()]
    if len(numbers) < 2:
        print("Ошибка: нужно минимум 2 числа")
        return
    neg_sum = sum_otr(numbers)
    max_ind, min_ind = max_min_index(numbers)
    product = product_between(numbers, max_ind, min_ind)

    print(f"\nРезультаты:")
    print(f"1. Сумма отрицательных элементов: {neg_sum}")
    print(f"2. Максимальный элемент: {numbers[max_ind]} (индекс {max_ind})")
    print(f"3. Минимальный элемент: {numbers[min_ind]} (индекс {min_ind})")
    if product is not None:
        print(f"4. Произведение элементов между ними: {product}")
    else:
        print(f"4. Нет элементов между максимальным и минимальным")

if __name__ == "__main__":
    main()