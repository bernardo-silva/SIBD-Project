#!/usr/bin/python3
import sys
sys.path.insert(0, "/home/bs/Cloud/5_ano/1_semestre/sibd/project/part3")

from utils import print_html, connect_to_database, Action
from utils import get_button, get_html_table
import cgi
import sys

sys.path.insert(0, "/home/bs/Cloud/5_ano/1_semestre/sibd/project/part3")
from credentials import host, port, IST_ID, password, db_name


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
        connection.commit()

        # CONVERT THIS TO SINGLE QUERY
        if senior == "senior":
            query2 = "INSERT INTO senior VALUES (%s);"
        elif senior == "junior":
            query2 = "INSERT INTO junior VALUES (%s);"

        cursor.execute(query2, (email,))
        connection.commit()

        print_html(query % data, "Sailor added", "SAILORS")

    except Exception as e:
        print_html(
            f"<h1>An error occurred!</h1><p>{e}</p>", "Error", "SAILORS")
    finally:
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    add_sailor_update()
