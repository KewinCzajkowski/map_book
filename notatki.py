import psycopg2
import requests
from bs4 import BeautifulSoup

db_params = psycopg2.connect(
    database="postgres",
    user="postgres",
    password='postgres',
    host="localhost",
    port="5432"
)

def get_coords(miejscowosc)-> list:
    url: str = f"https://pl.wikipedia.org/wiki/{miejscowosc}"
    response = requests.get(url)
    response_html = BeautifulSoup(response.text, 'html.parser')
    latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
    longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
    return [latitude, longitude]
def add_new_to_table(db_params) -> None:
    imie = input('Imie: ')
    nazwisko = input('Nazwisko: ')
    post = input('Post: ')
    miejscowosc = input('Miejscowosc: ')

    longitude,latidute=get_coords(miejscowosc)


    sql_add_query = f"INSERT INTO public.users(name, surname, post, location, coords)VALUES ('{imie}', '{nazwisko}', '{post}', '{miejscowosc}', 'SRID=4326;POINT({longitude} {latitude})');"
    cursor = db_params.cursor()
    cursor.execute(sql_add_query)
    db_params.commit()

# add_new_to_table(db_params)

def show_users(db_params) -> None:
    sql_add_query = f"SELECT * FROM public.users"
    cursor = db_params.cursor()
    cursor.execute(sql_add_query)
    users = cursor.fetchall()
    for user in users:
        print(user)


def remove_users(db_params) -> None:
    cursor = db_params.cursor()
    sql_remove_query = f"DELETE FROM public.users where name='{input('Imie: ')}'; "
    cursor.execute(sql_remove_query)
    db_params.commit()

def get_user_id(db_params) -> int:
    print('kogo aktualizować')
    sql_add_query = f"SELECT * FROM public.users where name='{input('Imie: ')}'"
    cursor = db_params.cursor()
    cursor.execute(sql_add_query)
    users = cursor.fetchall()[0][0]
    print(id)
    return id

def update_users(db_params) -> None:
    cursor = db_params.cursor()
    imie = input('new Imie: ')
    nazwisko = input('new Nazwisko: ')
    post = input('new Post: ')
    miejscowosc = input('new Miejscowosc: ')

    longitude,latidute = get_coords(miejscowosc)

    sql_update_query = f"UPDATE public.users SET name='{imie}', surname='{nazwisko}', post='{int(post)}',location='{miejscowosc}',coords='SRID=4326;POINT({longitude} {latitude})' WHERE id={get_user_id()}"
    cursor.execute(sql_update_query)
    db_params.commit()


update_users(db_params)

