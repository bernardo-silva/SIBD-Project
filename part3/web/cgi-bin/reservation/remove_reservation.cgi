#!/usr/bin/python3
import sys
sys.path.insert(0, "/afs/.ist.utl.pt/users/6/5/ist193365/web/sibd")

from utils import print_html, get_button
import cgi


def remove_reservation_form():
    try:
        form = cgi.FieldStorage()
        start_date = form.getvalue('start_date')
        end_date = form.getvalue('end_date')
        country = form.getvalue('country')
        cni = form.getvalue('cni')

        confirmation = f"\n<p> Are you sure you want to remove the reservation \
of boat {cni} from {country} between {start_date} and {end_date} and all associated trips?</p>"

        button = get_button("Remove",
                            f"remove_reservation_update.cgi?start_date={start_date}&\
end_date={end_date}&country={country}&cni={cni}",
                            color="danger")

        cancel_button = get_button("Cancel", "reservation.cgi", color="secondary")

        body = '<div class="text-center">\n' + confirmation + button + cancel_button + '</div>'

        print_html(body, "Remove reservation", active="RESERVATIONS")

    except Exception as e:
        print_html("", "An error occurred!", "RESERVATIONS")


if __name__ == "__main__":
    remove_reservation_form()
