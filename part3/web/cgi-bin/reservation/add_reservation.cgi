#!/usr/bin/python3
import sys
sys.path.insert(0, "/afs/.ist.utl.pt/users/6/5/ist193365/web/sibd")

from utils import print_html, get_form, connect_to_database
from credentials import host, port, IST_ID, password, db_name


def add_reservation_form():
    try:
        connection = connect_to_database(host, port, IST_ID, password, db_name)
        cursor = connection.cursor()

        boat_query = "SELECT country, cni FROM boat;"
        cursor.execute(boat_query)
        boats = cursor.fetchall()

        senior_query = "SELECT * FROM senior;"
        cursor.execute(senior_query)
        senior = cursor.fetchall()

        connection.close()

        form = get_form(entries=["start_date", "end_date"],
                        labels=["Start date:", "End date:"],
                        types=["date", "date"],
                        action="add_reservation_update.cgi",
                        selects=[dict(name='boat', options=boats, label="Boat"),
                                 dict(name='responsible', options=senior, label="Responsible email")])

        print_html(form, "Add new reservation", active="RESERVATIONS")

    except Exception as e:
        print_html(f"<h1>An error occurred!</h1><p>{e}</p>", "Error",
                   active="RESERVATIONS")


if __name__ == "__main__":
    add_reservation_form()
