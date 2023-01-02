#!/usr/bin/python3
import sys
import cgi
sys.path.insert(0, "/home/bs/Cloud/5_ano/1_semestre/sibd/project/part3")

from utils import print_html, get_form


def authorise_sailor():
    try:
        form = cgi.FieldStorage()
        start_date = form.getvalue('start_date')
        end_date = form.getvalue('end_date')
        country = form.getvalue('country')
        cni = form.getvalue('cni')

        form = get_form(entries=["sailor_email"],
                        labels=["Sailor email:"],
                        types=["email"],
                        action=f"/cgi-bin/reservation/authorise_sailor_update.cgi?start_date={start_date}&\
end_date={end_date}&country={country}&cni={cni}")

        print_html(form, "Authorise sailor", active="RESERVATIONS")

    except Exception as e:
        print_html(f"<h1>An error occurred!</h1><p>{e}</p>", "Error",
                   active="RESERVATIONS")


if __name__ == "__main__":
    authorise_sailor()
