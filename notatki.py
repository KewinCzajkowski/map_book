from models.data import users
from utils.crud import show_users

class User:
    def __init__(self,name,surname,posts,location):
        self.name=name
        self.surname=surname
        self.posts=posts
        self.location=location

user_1=User(name="<Kewin>",surname="<Czajkowski>",posts=10,location="Gdynia")
user_2=User(name="<Tomek>",surname="<Borowiecki>",posts=3,location="Warszawa")
print(user_2.name)

def update_user(users)-> None:
    kogo_szukasz=input("Kogo szukasz?: ")
    for user in users:
        if  user['name']==kogo_szukasz:
            user['name']=input("Podaj nowe imię: ")
            user['surname']=input("Podaj nowe nazwisko: ")
            user['liczba_postów']=input("Podaj liczbę postów: ")
print(users)
update_user(users)
print(users)