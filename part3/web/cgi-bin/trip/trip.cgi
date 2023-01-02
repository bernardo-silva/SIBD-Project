#!/usr/bin/python3
import sys
sys.path.insert(0, "/afs/.ist.utl.pt/users/6/5/ist193365/web/sibd")

from credentials import host, port, IST_ID, password, db_name
from utils import print_html, connect_to_database, Action
from utils import get_button, get_html_table


def trip():
    try:
        connection = connect_to_database(host, port, IST_ID, password, db_name)
        cursor = connection.cursor()

        query = "SELECT * FROM trip;"
        cursor.execute(query)
        result = cursor.fetchall()

        action = Action(description="Remove trip",
                        script="remove_trip.cgi",
                        parameters=["takeoff", "reservation_start_date",
                                    "reservation_end_date", "boat_country",
                                    "cni"],
                        columns=[0, 8, 9, 10, 11])

        table = get_html_table(result,
                                ["Takeoff Date", "Arrival Date", "Insurance Ref",
                                 "Origin Lat.", "Origin Long.",
                                 "Destination Lat.", "Destination Long.",
                                 "Skipper Email",
                                 "Reservation Start Date", "Reservation End Date",
                                 "Boat Country", "Boat CNI",""],
                               [action])

        add_trip_btn = get_button("Add trip <b>+</b>",
                                    "add_trip.cgi")

        print_html(table + add_trip_btn, "TRIPS", "TRIPS")
    except Exception as e:
        print_html(
            f"<h1>An error occurred!</h1><p>{e}</p>", "TRIPS", "TRIPS")
    finally:
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    trip()
