#!/usr/bin/python3
import sys
sys.path.insert(0, "/home/bs/Cloud/5_ano/1_semestre/sibd/project/part3")

from credentials import host, port, IST_ID, password, db_name
import cgi
from utils import print_html, connect_to_database


def deauthorise_sailor_update():
    try:
        form = cgi.FieldStorage()
        start_date = form.getvalue('start_date')
        end_date = form.getvalue('end_date')
        country = form.getvalue('country')
        cni = form.getvalue('cni')
        email = form.getvalue('sailor_email')

        data = (start_date, end_date, country, cni, email)

        connection = connect_to_database(host, port, IST_ID, password, db_name)
        cursor = connection.cursor()

        query = "DELETE FROM authorised WHERE start_date=%s AND end_date=%s AND\
         boat_country=%s AND cni=%s AND sailor=%s;"
        cursor.execute(query, data)
        connection.commit()

        print_html(query % data, "Sailor deauthorised", "RESERVATIONS")

    except Exception as e:
        print_html(
            f"<h1>An error occurred!</h1><p>{e}</p>", "Error", "RESERVATIONS")
    finally:
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    deauthorise_sailor_update()
