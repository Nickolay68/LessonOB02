class User:
    def __init__(self, user_id, name):
        # Защищенные атрибуты, к которым можно получить доступ только через методы класса
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    # Методы для получения значений атрибутов
    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    # Метод для изменения имени пользователя
    def set_name(self, name):
        self._name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'

    # Метод для добавления пользователя в систему (список users_list)
    def add_user(self, users_list, user):
        if isinstance(user, User):
            users_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Ошибка: добавляемый объект не является пользователем.")

    # Метод для удаления пользователя из системы по ID
    def remove_user(self, users_list, user_id):
        for user in users_list:
            if user.get_user_id() == user_id:
                users_list.remove(user)
                print(f"Пользователь с ID {user_id} удален.")
                return
        print(f"Пользователь с ID {user_id} не найден.")


# Пример использования
if __name__ == "__main__":
    # Создаем список для хранения пользователей
    users_list = []

    # Создаем администратора
    admin = Admin(1, "Алёна")

    # Создаем обычных пользователей
    user1 = User(2, "Николай")
    user2 = User(3, "Володя")

    # Администратор добавляет пользователей в список
    admin.add_user(users_list, user1)
    admin.add_user(users_list, user2)

    # Выводим информацию о всех пользователях в системе
    print("\nТекущие пользователи в системе:")
    for user in users_list:
        print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

    # Администратор удаляет пользователя по ID
    admin.remove_user(users_list, 2)

    # Выводим информацию о пользователях после удаления
    print("\nПользователи после удаления:")
    for user in users_list:
        print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")
