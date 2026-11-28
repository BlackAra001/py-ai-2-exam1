def add_hall(halls):
    print("\n--- Добавление кинозала ---")
    name = input("Название зала: ").strip()
    if not name:
        print("Ошибка: Название не может быть пустым.")
        return
    try:
        rows = int(input("Количество рядов: "))
        seats = int(input("Мест в ряду: "))
        if rows <= 0 or seats <= 0:
            raise ValueError
    except ValueError:
        print("Ошибка: Числа должны быть положительными.")
        return

    new_id = 1 if not halls else halls[-1]["id"] + 1
    halls.append({"id": new_id, "name": name, "rows": rows, "seats_per_row": seats})
    print(f"Зал '{name}' добавлен (ID: {new_id}).")

def show_halls(halls):
    print("\n--- Список залов ---")
    if not halls:
        print("Список пуст.")
        return
    for h in halls:
        print(f"ID: {h['id']} | {h['name']} | Рядов: {h['rows']} | Мест: {h['seats_per_row']}")