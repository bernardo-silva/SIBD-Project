#!/usr/bin/python3
import sys
sys.path.insert(0, "/home/bs/Cloud/5_ano/1_semestre/sibd/project/part3")

from utils import print_html, get_form


def add_reservation_form():
    try:
        form = get_form(entries=["start_date", "end_date", "country", "cni",
                                 "responsible"],
                        labels=["Start date:", "End date:", "Country:", "CNI:",
                                "Responsible:"],
                        types=["date", "date", "text", "text", "email"],
                        action="/cgi-bin/reservation/add_reservation_update.cgi")

        print_html(form, "Add new reservation", active="RESERVATIONS")

    except Exception as e:
        print_html(f"<h1>An error occurred!</h1><p>{e}</p>", "Error",
                   active="RESERVATIONS")


if __name__ == "__main__":
    add_reservation_form()
