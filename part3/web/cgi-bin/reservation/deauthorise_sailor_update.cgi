#!/usr/bin/python3
import sys
sys.path.insert(0, "/afs/.ist.utl.pt/users/6/5/ist193365/web/sibd")

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

        body = '<div class="text-center">\n'
        body += f'<p>{" | ".join(data)}</p>\n'
        body += '</div>\n'

        print_html(body, "Sailor deauthorised", "RESERVATIONS")

    except Exception as e:
        print_html("", "An error occurred!", "RESERVATIONS")
        connection.rollback()

    finally:
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    deauthorise_sailor_update()
