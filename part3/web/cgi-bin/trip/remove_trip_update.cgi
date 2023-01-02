#!/usr/bin/python3
import sys
sys.path.insert(0, "/afs/.ist.utl.pt/users/6/5/ist193365/web/sibd")

from utils import print_html, connect_to_database, Action
from utils import get_button, get_html_table
import cgi
from credentials import host, port, IST_ID, password, db_name


def add_sailor_update():
    try:
        form = cgi.FieldStorage()
        takeoff = form.getvalue("takeoff")
        reservation_start_date = form.getvalue("reservation_start_date")
        reservation_end_date = form.getvalue("reservation_end_date")
        boat_country = form.getvalue("boat_country")
        cni = form.getvalue("cni")

        data = (takeoff, reservation_start_date, reservation_end_date, boat_country, cni)

        connection = connect_to_database(host, port, IST_ID, password, db_name)
        cursor = connection.cursor()

        query= "DELETE FROM trip WHERE takeoff=%s AND reservation_start_date=%s AND reservation_end_date=%s AND boat_country=%s AND cni=%s;"
        cursor.execute(query, data)

        connection.commit()

        print_html(query % data, "Trip removed", "TRIPS")

    except Exception as e:
        print_html(
            f"<h1>An error occurred!</h1><p>{e}</p>", "Error", "TRIPS")
    finally:
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    add_sailor_update()
