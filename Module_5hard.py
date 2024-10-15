class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    users = {}
    videos = {}

    def __new__(cls, *args, **kwargs):
        cls.users.update(kwargs)
        return object.__new__(cls)

    def __init__(self, users, videos, current_user=User):
        self.users = users
        self.videos = videos
        self.current_user = current_user

        def log_in(nickname, password):
            my_dict = users
            for key, value in my_dict.items():
                print(value)