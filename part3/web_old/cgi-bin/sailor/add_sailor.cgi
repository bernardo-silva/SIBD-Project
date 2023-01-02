#!/usr/bin/python3
import sys
sys.path.insert(0, "/home/bs/Cloud/5_ano/1_semestre/sibd/project/part3")

from utils import print_html, get_form


def add_sailor_form():
    try:
        form = get_form(entries=["email", "firstname", "surname"],
                        labels=["E-mail:", "First name:", "Surname:"],
                        types=["email", "text", "text"],
                        action="/cgi-bin/sailor/add_sailor_update.cgi",
                        radios=[dict(name="senior",
                                    entries=("senior", "junior"),
                                    labels=("Senior", "Junior"),
                                    rtype="radio")]
                        )

        print_html(form, "Add new sailor", active="SAILORS")

    except Exception as e:
        print_html(f"<h1>An error occurred!</h1><p>{e}</p>", "Error",
                   active="SAILORS")


if __name__ == "__main__":
    add_sailor_form()
