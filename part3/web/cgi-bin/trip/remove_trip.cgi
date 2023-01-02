#!/usr/bin/python3
import cgi
import sys
sys.path.insert(0, "/afs/.ist.utl.pt/users/6/5/ist193365/web/sibd")

from utils import print_html, get_button


def remove_trip_form():
    try:
        form = cgi.FieldStorage()
        takeoff = form.getvalue("takeoff")
        reservation_start_date = form.getvalue("reservation_start_date")
        reservation_end_date = form.getvalue("reservation_end_date")
        boat_country = form.getvalue("boat_country")
        cni = form.getvalue("cni")

        confirmation = "\n<p> Are you sure you want to remove this trip?</p>"

        confirm_button = get_button("Remove",
                                    f"remove_trip_update.cgi?takeoff={takeoff}&reservation_start_date={reservation_start_date}&reservation_end_date={reservation_end_date}&boat_country={boat_country}&cni={cni}",
                                    color="danger")
        cancel_button = get_button("Cancel", "trip.cgi", color="secondary")

        body = '<div class="text-center">\n' + confirmation + confirm_button + cancel_button + '</div>'

        print_html(body, "Remove trip", active="TRIPS")

    except Exception as e:
        print_html(f"<h1>An error occurred!</h1><p>{e}</p>", "Error",
                   active="TRIPS")


if __name__ == "__main__":
    remove_trip_form()
