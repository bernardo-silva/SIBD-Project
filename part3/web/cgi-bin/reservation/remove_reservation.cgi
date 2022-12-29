#!/usr/bin/python3
import sys
sys.path.insert(0, "/home/bs/Cloud/5_ano/1_semestre/sibd/project/part3")

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
of boat {cni} from {country} between {start_date} and {end_date}?</p>"

        button = get_button("Remove",
                            f"/cgi-bin/reservation/remove_reservation_update.cgi?start_date={start_date}&\
end_date={end_date}&country={country}&cni={cni}",
                            color="danger")

        cancel_button = get_button("Cancel",
                                   "/cgi-bin/reservation/reservation.cgi")
        
        print_html(confirmation + button + cancel_button, "Remove reservation",
                   active="RESERVATIONS")

    except Exception as e:
        print_html(f"<h1>An error occurred!</h1><p>{e}</p>", "Error",
                   active="RESERVATIONS")


if __name__ == "__main__":
    remove_reservation_form()
