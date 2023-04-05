#!/usr/bin/python3
import sys
sys.path.insert(0, "/afs/.ist.utl.pt/users/6/5/ist193365/web/sibd")

from utils import print_html, connect_to_database, Action
from utils import get_html_table, get_button
from credentials import host, port, IST_ID, password, db_name


def reservations():
    try:
        connection = connect_to_database(host, port, IST_ID, password, db_name)
        cursor = connection.cursor()

        query = "SELECT * FROM reservation;"
        cursor.execute(query)
        result = cursor.fetchall()

        action_remove = Action(description="Remove reservation",
                               script="remove_reservation.cgi",
                               parameters=["start_date", "end_date", "country",
                                           "cni"],
                               columns=[0, 1, 2, 3])

        action_authorize = Action(description="Authorise Sailors",
                                  script="authorise_sailor.cgi",
                                  parameters=["start_date", "end_date", "country",
                                              "cni"],
                                  columns=[0, 1, 2, 3])

        action_deauthorize = Action(description="Deauthorise Sailors",
                                    script="deauthorise_sailor.cgi",
                                    parameters=["start_date", "end_date", "country",
                                                "cni"],
                                    columns=[0, 1, 2, 3])

        table = get_html_table(result,
                               ["Start Date", "End Date", "Boat Country",
                                   "Boat CNI", "Responsible Sailor", "", "", ""],
                               [action_remove, action_authorize, action_deauthorize])

        add_reservation_btn = get_button("Add reservation <b>+</b>",
                                    "add_reservation.cgi")

        print_html(table + add_reservation_btn, "RESERVATIONS", "RESERVATIONS")
    except Exception as e:
        print_html("", "An error occurred!", "RESERVATIONS")
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    reservations()
