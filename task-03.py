def hanoi(n, start, end, temp, state):
    if n == 1:
        print(f"Перемістити диск з {start} на {end}: 1")
        state[start].pop()
        state[end].append(1)
        print(f"Проміжний стан: {state}")
        return
    # Переміщення n-1 дисків на тимчасовий стрижень
    hanoi(n - 1, start, temp, end, state)

    # Переміщення найбільшого диска на кінцевий стрижень
    print(f"Перемістити диск з {start} на {end}: {n}")
    state[start].pop()
    state[end].append(n)
    print(f"Проміжний стан: {state}")

    # Переміщення n-1 дисків з тимчасового стрижня на кінцевий
    hanoi(n - 1, temp, end, start, state)

def main():
    n = int(input("Введіть кількість дисків: "))
    state = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}  # Стартовий стан: усі диски на стрижні A
    print(f"Початковий стан: {state}")
    hanoi(n, 'A', 'C', 'B', state)
    print(f"Кінцевий стан: {state}")

if __name__ == "__main__":
    main()
