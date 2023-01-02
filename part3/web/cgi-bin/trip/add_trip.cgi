#!/usr/bin/python3
import sys
sys.path.insert(0, "/afs/.ist.utl.pt/users/6/5/ist193365/web/sibd")


from utils import print_html, get_form, connect_to_database
from credentials import host, port, IST_ID, password, db_name


def add_trip_form():
    try:
        connection = connect_to_database(host, port, IST_ID, password, db_name)
        cursor = connection.cursor()

        reservation_query = "SELECT start_date, end_date, country, cni FROM reservation;"
        cursor.execute(reservation_query)
        reservations = cursor.fetchall()

        location_query = "SELECT name, latitude, longitude FROM location;"
        cursor.execute(location_query)
        locations = cursor.fetchall()

        sailor_query = "SELECT email FROM sailor;"
        cursor.execute(sailor_query)
        sailors = cursor.fetchall()

        connection.close()

        form = get_form(entries=["takeoff", "arrival", "insurance", "skipper"],
                        labels=["Takeoff Date", "Arrival Date", "Insurance Ref"],
                        types=["date", "date", "text"],
                        action="add_trip_update.cgi",
                        selects=[dict(name='reservation', options=reservations, label="Reservation"),
                                 dict(name='from_location', options=locations, label="From Location"),
                                 dict(name='to_location', options=locations, label="To Location"),
                                 dict(name='skipper', options=sailors, label="Skipper Email")]
                        )

        print_html(form, "Add new trip", active="TRIPS")

    except Exception as e:
        print_html(f"<h1>An error occurred!</h1><p>{e}</p>", "Error",
                   active="TRIPS")


if __name__ == "__main__":
    add_trip_form()
