def add_movie(movies):
    title = input("Название: ").strip()
    if not title:
        print("Ошибка: Название не может быть пустым.")
        return
    genre = input("Жанр: ").strip()
    try:
        duration = int(input("Продолжительность (мин): "))
        if duration <= 0:
            raise ValueError
    except ValueError:
        print("Ошибка: Продолжительность должна быть положительным числом.")
        return

    new_id = 1 if not movies else movies[-1]["id"] + 1
    movies.append({"id": new_id, "title": title, "genre": genre, "duration": duration})
    print(f"Фильм '{title}' добавлен (ID: {new_id}).")

def show_movies(movies):
    if not movies:
        print("Список пуст.")
        return
    for m in movies:
        print(f"ID: {m['id']} | {m['title']} | {m['genre']} | {m['duration']} мин.")

def delete_movie(movies):
    if not movies:
        print("Список пуст.")
        return
    try:
        movie_id = int(input("Введите ID фильма: "))
    except ValueError:
        print("Ошибка: ID должен быть числом.")
        return
    for m in movies:
        if m["id"] == movie_id:
            movies.remove(m)
            print("Фильм удален.")
            return
    print("Фильм с таким ID не найден.")
