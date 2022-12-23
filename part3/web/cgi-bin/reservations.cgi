#!/usr/bin/python3

from utils import print_html, get_html_table, connect_to_database, Action
import sys

sys.path.insert(0, "/home/bs/Cloud/5_ano/1_semestre/sibd/project/part3")
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

        action_authorize = Action(description="Authorize Sailors",
                                  script="authorize_sailors.cgi",
                                  parameters=["start_date", "end_date", "country",
                                              "cni"],
                                  columns=[0, 1, 2, 3])

        action_deauthorize = Action(description="Deauthorize Sailors",
                                    script="deauthorize_sailors.cgi",
                                    parameters=["start_date", "end_date", "country",
                                                "cni"],
                                    columns=[0, 1, 2, 3])

        table = get_html_table(result,
                               ["Start Date", "End Date", "Boat Country",
                                   "Boat CNI", "Responsible Sailor", "", "", ""],
                               [action_remove, action_authorize, action_deauthorize])

        print_html(table, "RESERVATIONS", "RESERVATIONS")
    except Exception as e:
        print_html(
            f"<h1>An error occurred!</h1><p>{e}</p>", "RESERVATIONS", "RESERVATIONS")
    finally:
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    reservations()
