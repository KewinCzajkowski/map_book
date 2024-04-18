users: list[dict] = [
    {"name": "Dawid", "surname": "Bałuka", "posts": 6000},
    {"name": "Kewin", "surname": "Czajkowski", "posts": 6002},
    {"name": "Kamil", "surname": "Gil", "posts": 1_000_000},
    {"name": "Daniel", "surname": "Błaszczyk", "posts": 6}

]


def show_users(user_list: list[dict]) -> None:
    for user in user_list:
        print(f"Twój znajomy {user['name']} opublikował: {user['posts']} postów")

show_users(users)