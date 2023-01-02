#!/usr/bin/python3
import sys
sys.path.insert(0, "/afs/.ist.utl.pt/users/6/5/ist193365/web/sibd")

from utils import print_html, connect_to_database, Action
from utils import get_button, get_html_table
import cgi
import sys

sys.path.insert(0, "/home/bs/Cloud/5_ano/1_semestre/sibd/project/part3")
from credentials import host, port, IST_ID, password, db_name


def add_trip_update():
    try:
        form = cgi.FieldStorage()
        takeoff = form.getvalue('takeoff')
        arrival = form.getvalue('arrival')
        insurance = form.getvalue('insurance')
        _, from_latitude, from_longitude  = form.getvalue('from_location').split(";")
        _, to_latitude, to_longitude  = form.getvalue('to_location').split(";")
        skipper = form.getvalue('skipper')
        reservation = form.getvalue('reservation').split(";")

        data = (takeoff, arrival, insurance, from_latitude, from_longitude,
                to_latitude, to_longitude, skipper, *reservation)

        connection = connect_to_database(host, port, IST_ID, password, db_name)
        cursor = connection.cursor()

        query = "INSERT INTO trip VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(query, data)

        connection.commit()

        print_html(query % data, "Trip added", "TRIPS")

    except Exception as e:
        print_html(
            f"<h1>An error occurred!</h1><p>{e}</p>", "Error", "TRIPS")
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    add_trip_update()
