def add_session(sessions, movies, halls):
    print("\n--- Создание сеанса ---")
    if not movies or not halls:
        print("Ошибка: Сначала добавьте фильмы и залы.")
        return
    
    print("Доступные фильмы:")
    for m in movies: 
        print(f"ID: {m['id']} | {m['title']}")
        
    print("Доступные залы:")
    for h in halls: 
        print(f"ID: {h['id']} | {h['name']}")
    
    try:
        movie_id = int(input("Введите ID фильма: "))
        hall_id = int(input("Введите ID зала: "))
        
        if not any(m["id"] == movie_id for m in movies) or not any(h["id"] == hall_id for h in halls):
            print("Ошибка: Неверный ID фильма или зала.")
            return
    except ValueError:
        print("Ошибка: ID должны быть числами.")
        return

    date = input("Дата (ГГГГ-ММ-ДД): ").strip()
    time = input("Время (ЧЧ:ММ): ").strip()
    if not date or not time:
        print("Ошибка: Дата и время обязательны.")
        return

    new_id = 1 if not sessions else sessions[-1]["id"] + 1
    sessions.append({"id": new_id, "movie_id": movie_id, "hall_id": hall_id, "date": date, "time": time})
    print(f"Сеанс успешно создан (ID: {new_id}).")

def show_sessions(sessions, movies, halls):
    print("\n--- Расписание сеансов ---")
    if not sessions:
        print("Расписание пусто.")
        return
        
    for s in sessions:
        movie_name = next((m["title"] for m in movies if m["id"] == s["movie_id"]), "Неизвестно")
        hall_name = next((h["name"] for h in halls if h["id"] == s["hall_id"]), "Неизвестно")
        print(f"ID: {s['id']} | {movie_name} | {hall_name} | {s['date']} в {s['time']}")