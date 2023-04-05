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
        email = form.getvalue('email')

        connection = connect_to_database(host, port, IST_ID, password, db_name)
        cursor = connection.cursor()

        query_senior = "DELETE FROM senior WHERE email=%s;"
        cursor.execute(query_senior, (email,))

        query_junior = "DELETE FROM junior WHERE email=%s;"
        cursor.execute(query_junior, (email,))

        query = "DELETE FROM sailor WHERE email=%s;"
        cursor.execute(query, (email,))

        connection.commit()

        body = '<div class="text-center">\n'
        body += f'<p>{email}</p>\n'
        body += '</div>\n'

        print_html(body, "Sailor removed", "SAILORS")

    except Exception as e:
        print_html("", "An error occurred!", "SAILORS")
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    add_sailor_update()
