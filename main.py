from models.data import users
from utils.crud import show_users


if __name__ == "__main__":
    print("Witaj użytkowniku")
    while True:
        print("Menu:")
        print("1. Wyswietl co u znajomych")
        menu_option: str = input("Dokonaj wyboru:")
        if menu_option == "0":
            print("Program kończy prace")
            break
        if menu_option == "1":
            show_users(users)
