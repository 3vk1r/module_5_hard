import time
class User:
    def __init__(self, username, password, age):
        self.username = username
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password):
        return hash(password)

    def __str__(self):
        return f"Пользователь: {self.username}, возраст: {self.age}"

    def __repr__(self):
        return f"User(nickname={self.username}, age={self.age})"

    def __eq__(self, other):
        if isinstance(other, User):
            return self.username == other.username and self.password == other.password
        return False
class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return f"Видео: {self.title}, продолжительность: {self.duration} секунд"

    def __repr__(self):
        return f"Video(title={self.title}, duration={self.duration}, adult_mode={self.adult_mode})"

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title
        return False

    def __contains__(self, keyword: str):
        return keyword.lower() in self.title.lower()
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, username: str, password: str, age: int):
        if any(user.username == username for user in self.users):
            print(f"Пользователь {username} уже существует")
            return
        new_user = User(username, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {username} зарегистрирован и вошёл в систему")

    def log_out(self):
        if self.current_user:
            print(f"Пользователь {self.current_user.username} вышел из системы")
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)
                print(f"Видео '{video.title}' добавлено на платформу")
            else:
                print(f"Видео '{video.title}' уже существует")

    def get_videos(self, search_term: str):
        matching_videos = [video.title for video in self.videos if search_term in video]
        return matching_videos

    def watch_video(self, title: str):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video = next((v for v in self.videos if v.title == title), None)
        if not video:
            print(f"Видео '{title}' не найдено")
            return

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        print(f"Начинается воспроизведение видео '{video.title}'")
        for second in range(video.time_now, video.duration):
            print(f"Секунда: {second + 1}")
            time.sleep(1)  # Задержка для имитации просмотра видео
        video.time_now = 0
        print("Конец видео")

    def __str__(self):
        return f"UrTube: пользователей {len(self.users)}, видео {len(self.videos)}"

    def __repr__(self):
        return f"UrTube(users={len(self.users)}, videos={len(self.videos)})"
    def log_in(self, nickname: str, password: str):
        hashed_password = hash(password)  # Хэшируем введённый пароль
        for user in self.users:
            if user == User(nickname, password, 0):  # Проверяем по никнейму и паролю
                self.current_user = user
                print(f"Пользователь {nickname} вошёл в систему")
                return
        print("Неверный логин или пароль")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
