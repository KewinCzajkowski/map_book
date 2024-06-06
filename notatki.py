import psycopg2

from utils.crud import show_users

db_params=psycopg2.connect(
    database="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432",
)

def add_user_to_table(db_params)->None:
    imie=input("Imie: ")
    nazwisko=input("Nazwisko: ")
    post=input("Post: ")
    miejscowosc=input("Miejscowosc: ")

    sql_add_query=f"INSERT INTO public.users(name, surname, post, location, coords) VALUES ( '{imie}', '{nazwisko}', {post}, '{miejscowosc}', 'SRID=4326;POINT(21.0 52.23)');"
    cursor=db_params.cursor()
    cursor.execute(sql_add_query)
    db_params.commit()

# add_user_to_table(db_params)

    def show_users(db_params)->None:

        sql_add_query = f"SELECT * FROM public.users"
        cursor = db_params.cursor()
        cursor.execute(sql_add_query)
        db_params.commit()
        users=cursor.fetchall()
        # print(users)
        # db_params.close()
        for user in users:
            print(user)
show_users(db_params)
