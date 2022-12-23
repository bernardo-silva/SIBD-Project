#!/usr/bin/python3

from utils import print_html, connect_to_database, Action
from utils import get_button, get_html_table
import sys

sys.path.insert(0, "/home/bs/Cloud/5_ano/1_semestre/sibd/project/part3")
from credentials import host, port, IST_ID, password, db_name


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

        add_sailor_btn = get_button("Add sailor <b>+</b>", "/cgi-bin/add_sailor.cgi")

        print_html(table + add_sailor_btn, "SAILORS", "SAILORS")
    except Exception as e:
        print_html(
            f"<h1>An error occurred!</h1><p>{e}</p>", "SAILORS", "SAILORS")
    finally:
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    sailors()
