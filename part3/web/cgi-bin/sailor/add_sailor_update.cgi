#!/usr/bin/python3
import sys
sys.path.insert(0, "/afs/.ist.utl.pt/users/6/5/ist193365/web/sibd")

from utils import print_html, connect_to_database, Action
from utils import get_button, get_html_table
from credentials import host, port, IST_ID, password, db_name
import cgi
import sys

def add_sailor_update():
    try:
        form = cgi.FieldStorage()
        firstname = form.getvalue('firstname')
        surname = form.getvalue('surname')
        email = form.getvalue('email')
        senior = form.getvalue('senior')

        data = (firstname, surname, email)

        connection = connect_to_database(host, port, IST_ID, password, db_name)
        cursor = connection.cursor()

        query = "INSERT INTO sailor VALUES (%s, %s, %s);"
        cursor.execute(query, data)

        if senior == "senior":
            query2 = "INSERT INTO senior VALUES (%s);"
        elif senior == "junior":
            query2 = "INSERT INTO junior VALUES (%s);"
        else:
            query2 = ""
            cursor.rollback()

        cursor.execute(query2, (email,))

        connection.commit()

        body = '<div class="text-center">\n'
        body += f'<p>{" | ".join(data)} | {"Senior" if senior else "Junior"}</p>\n'
        body += '</div>\n'

        print_html(body, "Sailor added", "SAILORS")

    except Exception as e:
        print_html("", "An error occurred!", "SAILORS")
        connection.rollback()

    finally:
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    add_sailor_update()
