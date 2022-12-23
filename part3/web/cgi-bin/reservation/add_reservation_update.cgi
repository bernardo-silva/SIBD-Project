#!/usr/bin/python3
import sys
sys.path.insert(0, "/home/bs/Cloud/5_ano/1_semestre/sibd/project/part3")

from credentials import host, port, IST_ID, password, db_name
import cgi
from utils import print_html, connect_to_database



def add_sailor_update():
    try:
        form = cgi.FieldStorage()
        start_date = form.getvalue('start_date')
        end_date = form.getvalue('end_date')
        country = form.getvalue('country')
        cni = form.getvalue('cni')
        responsible = form.getvalue('responsible')

        dates = [start_date, end_date]
        boat = [country, cni]

        connection = connect_to_database(host, port, IST_ID, password, db_name)
        cursor = connection.cursor()

        date_interval_query = "INSERT INTO date_interval VALUES (%s, %s);"
        cursor.execute(date_interval_query, dates)
        connection.commit()

        query = "INSERT INTO reservation VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(query, dates + boat + [responsible])
        connection.commit()

        print_html(query % (dates + boat + [responsible]),
                   "Reservation added", "SAILORS")

    except Exception as e:
        print_html(
            f"<h1>An error occurred!</h1><p>{e}</p>", "Error", "RESERVATIONS")
    finally:
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    add_sailor_update()
