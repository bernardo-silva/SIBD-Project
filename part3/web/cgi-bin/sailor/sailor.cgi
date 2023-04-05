#!/usr/bin/python3
import sys
sys.path.insert(0, "/afs/.ist.utl.pt/users/6/5/ist193365/web/sibd")

from credentials import host, port, IST_ID, password, db_name
from utils import print_html, connect_to_database, Action
from utils import get_button, get_html_table


def sailors():
    try:
        connection = connect_to_database(host, port, IST_ID, password, db_name)
        cursor = connection.cursor()

        query = "SELECT * FROM sailor;"
        cursor.execute(query)
        result = cursor.fetchall()

        action = Action(description="Remove sailor",
                        script="remove_sailor.cgi",
                        parameters=["email"],
                        columns=[2])

        table = get_html_table(result,
                               ["First Name", "Last Name", "E-mail", ""],
                               [action])

        add_sailor_btn = get_button("Add sailor <b>+</b>",
                                    "add_sailor.cgi")

        print_html(table + add_sailor_btn, "SAILORS", "SAILORS")
    except Exception as e:
        print_html("", "An error occurred!", "SAILORS")
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    sailors()
