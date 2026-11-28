def add_booking(bookings, sessions, halls):
    if not sessions:
        print("Нет сеансов.")
        return

    print("Доступные сеансы:")
    for s in sessions: 
        print(f"ID: {s['id']} | {s['date']} {s['time']}")
    
    try:
        session_id = int(input("ID сеанса: "))
    except ValueError:
        print("Ошибка: ID должен быть числом.")
        return

    session = next((s for s in sessions if s["id"] == session_id), None)
    if not session:
        print("Сеанс не найден.")
        return

    hall = next((h for h in halls if h["id"] == session["hall_id"]), None)
    
    customer = input("Имя клиента: ").strip()
    if not customer:
        print("Ошибка: Имя пустое.")
        return

    try:
        row = int(input("Ряд: "))
        seat = int(input("Место: "))
        if not (1 <= row <= hall["rows"] and 1 <= seat <= hall["seats_per_row"]):
            print("Ошибка: Места с таким номером не существует.")
            return
    except ValueError:
        print("Ошибка: Введите числа.")
        return

    for b in bookings:
        if b["session_id"] == session_id and b["row"] == row and b["seat"] == seat:
            print("Ошибка: Место уже занято!")
            return

    new_id = 1 if not bookings else bookings[-1]["id"] + 1
    bookings.append({"id": new_id, "session_id": session_id, "customer_name": customer, "row": row, "seat": seat})
    print(f"Место {row}-{seat} забронировано для {customer}.")

def show_bookings(bookings, sessions):
    if not bookings:
        print("Бронирований нет.")
        return
    for b in bookings:
        session = next((s for s in sessions if s["id"] == b["session_id"]), None)
        date_str = f"{session['date']} {session['time']}" if session else "?"
        print(f"ID: {b['id']} | {b['customer_name']} | Сеанс: {date_str} | Ряд: {b['row']} | Место: {b['seat']}")

def cancel_booking(bookings):
    if not bookings:
        print("Броней нет.")
        return
    try:
        b_id = int(input("ID брони: "))
    except ValueError:
        print("Ошибка: ID должен быть числом.")
        return
    for b in bookings:
        if b["id"] == b_id:
            bookings.remove(b)
            print("Бронь отменена.")
            return
    print("Бронь не найдена.")