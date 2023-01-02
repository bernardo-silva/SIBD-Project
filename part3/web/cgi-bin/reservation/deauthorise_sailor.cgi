#!/usr/bin/python3
import sys
import cgi
sys.path.insert(0, "/afs/.ist.utl.pt/users/6/5/ist193365/web/sibd")

from utils import print_html, get_form, connect_to_database
from credentials import host, port, IST_ID, password, db_name


def deauthorise_sailor():
    try:
        form = cgi.FieldStorage()
        start_date = form.getvalue('start_date')
        end_date = form.getvalue('end_date')
        country = form.getvalue('country')
        cni = form.getvalue('cni')

        connection = connect_to_database(host, port, IST_ID, password, db_name)
        cursor = connection.cursor()

        sailor_query = "SELECT sailor FROM authorised as a WHERE a.start_date = %s AND a.end_date = %s AND a.boat_country = %s AND a.cni = %s;"
        cursor.execute(sailor_query, (start_date, end_date, country, cni))
        sailors = cursor.fetchall()

        form = get_form(action=f"deauthorise_sailor_update.cgi?start_date={start_date}&\
end_date={end_date}&country={country}&cni={cni}",
                        selects=[dict(name='sailor_email', options=sailors, label="Sailor email")],
                        )

        print_html(form, "Deauthorise sailor", active="RESERVATIONS")

    except Exception as e:
        print_html(f"<h1>An error occurred!</h1><p>{e}</p>", "Error",
                   active="RESERVATIONS")


if __name__ == "__main__":
    deauthorise_sailor()
