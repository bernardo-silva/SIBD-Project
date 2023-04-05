#!/usr/bin/python3
import cgi
import sys
sys.path.insert(0, "/afs/.ist.utl.pt/users/6/5/ist193365/web/sibd")

from credentials import host, port, IST_ID, password, db_name
from utils import print_html, connect_to_database


def add_sailor_update():
    try:
        form = cgi.FieldStorage()
        start_date = form.getvalue('start_date')
        end_date = form.getvalue('end_date')
        boat = form.getvalue('boat')
        country, cni = boat.split(";")

        responsible = form.getvalue('responsible')

        dates = [start_date, end_date]
        boat = [country, cni]
        data = (*dates, *boat)

        connection = connect_to_database(host, port, IST_ID, password, db_name)
        cursor = connection.cursor()

        date_interval_query = "INSERT INTO date_interval VALUES (%s, %s);"
        cursor.execute(date_interval_query, dates)

        query = "INSERT INTO reservation VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(query, dates + boat + [responsible])

        connection.commit()

        body = '<div class="text-center">\n'
        body += f'<p>{" | ".join(data)}</p>\n'
        body += '</div>\n'

        print_html(body, "Reservation added", "RESERVATIONS")

    except Exception as e:
        print_html(
            f"<h1>An error occurred!</h1><p>{e}</p>", "Error", "RESERVATIONS")
    finally:
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    add_sailor_update()
