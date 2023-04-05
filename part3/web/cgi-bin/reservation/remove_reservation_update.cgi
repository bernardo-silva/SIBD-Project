#!/usr/bin/python3
import sys
sys.path.insert(0, "/afs/.ist.utl.pt/users/6/5/ist193365/web/sibd")

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

        query_trip = "DELETE FROM trip WHERE reservation_start_date=%s AND reservation_end_date=%s AND \
        boat_country=%s AND cni=%s;"
        cursor.execute(query_trip, data)

        query_authorised = "DELETE FROM authorised WHERE start_date=%s AND end_date=%s AND \
        boat_country=%s AND cni=%s;"
        cursor.execute(query_authorised, data)

        query = "DELETE FROM reservation WHERE start_date=%s AND end_date=%s AND \
        country=%s AND cni=%s;"
        cursor.execute(query, data)

        connection.commit()

        body = '<div class="text-center">\n'
        body += f'<p>{" | ".join(data)}</p>\n'
        body += '</div>\n'

        print_html(body, "Reservation removed", "RESERVATIONS")

    except Exception as e:
        print_html("", "An error occurred!", "RESERVATIONS")
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    remove_reservation_update()
