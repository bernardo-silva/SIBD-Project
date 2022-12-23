#!/usr/bin/python3
import sys
sys.path.insert(0, "/home/bs/Cloud/5_ano/1_semestre/sibd/project/part3")

from utils import print_html, connect_to_database
import cgi
from credentials import host, port, IST_ID, password, db_name


def remove_reservation_update():
    try:
        form = cgi.FieldStorage()
        start_date = form.getvalue('start_date')
        end_date = form.getvalue('end_date')
        country = form.getvalue('country')
        cni = form.getvalue('cni')
        data = (start_date, end_date, country, cni)

        connection = connect_to_database(host, port, IST_ID, password, db_name)
        cursor = connection.cursor()

        query = "DELETE FROM reservation WHERE start_date=%s AND end_date=%s AND \
        country=%s AND cni=%s;"
        cursor.execute(query, data)
        connection.commit()

        print_html(query % data, "Reservation removed", "RESERVATIONS")

    except Exception as e:
        print_html(
            f"<h1>An error occurred!</h1><p>{e}</p>", "Error", "RESERVATIONS")
    finally:
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    remove_reservation_update()
