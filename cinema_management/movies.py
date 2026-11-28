
from movies import add_movie, show_movies, delete_movie
from halls import add_hall, show_halls
from sessions import add_session, show_sessions
from bookings import add_booking, show_bookings, cancel_booking
def main():
    movies_list = []
    halls_list = []
    sessions_list = []
    bookings_list = []

    while True:
        print("\n===== CINEMA MANAGEMENT SYSTEM =====")
        print("1. Добавить фильм")
        print("2. Показать фильмы")
        print("3. Удалить фильм")
        print("4. Добавить кинозал")
        print("5. Показать кинозалы")
        print("6. Создать сеанс")
        print("7. Показать расписание")
        print("8. Забронировать место")
        print("9. Показать бронирования")
        print("10. Отменить бронирование")
        print("0. Выход")
        
        choice = input("Выберите действие: ")

        if choice == "1":
            add_movie(movies_list)
        elif choice == "2":
            show_movies(movies_list)
        elif choice == "3":
            delete_movie(movies_list)
        elif choice == "4":
            add_hall(halls_list)
        elif choice == "5":
            show_halls(halls_list)
        elif choice == "6":
            add_session(sessions_list, movies_list, halls_list)
        elif choice == "7":
            show_sessions(sessions_list, movies_list, halls_list)
        elif choice == "8":
            add_booking(bookings_list, sessions_list, halls_list)
        elif choice == "9":
            show_bookings(bookings_list, sessions_list)
        elif choice == "10":
            cancel_booking(bookings_list)
        elif choice == "0":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()