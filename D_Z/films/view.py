def add_title(title):
    def wrapper(funk):
        def wrap(*args):
            print(f"{title}".center(50, "="))
            output = funk(*args)
            print("=" * 50)
            return output

        return wrap

    return wrapper


class UserInterface:
    @add_title("Редактирование каталога фильмов")
    def wait_user_ansver(self):
        print("Действия со стотьями:")
        print("1 - добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определенного фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        user_answer = input("Вырор действия:")
        return user_answer

    @add_title("Добавление фильма")
    def add_user_film(self):
        dict_film = {
            "название фильма": None,
            "жанр": None,
            "режиссер": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актеры": None
        }
        for key in dict_film:
            dict_film[key] = input(f"введите {key}: ")
        return dict_film

    @add_title("список фильмов")
    def show_all_films(self, films):
        for ind, i in enumerate(films, start=1):
            print(f"{ind}. {i}")

    @add_title("Ввод название фильма")
    def get_user_film(self):
        user_film = input("введите название фильма")
        return user_film

    @add_title("Просмотр фильма")
    def show_film(self, film):
        for key in film:
            print(f"{key} - {film[key]}")

    @add_title("ошибка")
    def show_error(self, user_title):
        print(f"{user_title} такого ф ильма нет")

    @add_title("удаление фильма")
    def remuve_sinfle_film(self, film):
        print(f"фильм: {film} удален")

    def show_answe_error(self, answer):
        print(f"Вариант {answer} не существует")