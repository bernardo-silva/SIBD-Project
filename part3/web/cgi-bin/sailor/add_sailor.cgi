#!/usr/bin/python3
import sys
sys.path.insert(0, "/afs/.ist.utl.pt/users/6/5/ist193365/web/sibd")


from utils import print_html, get_form


def add_sailor_form():
    try:
        form = get_form(entries=["email", "firstname", "surname"],
                        labels=["E-mail:", "First name:", "Surname:"],
                        types=["email", "text", "text"],
                        action="add_sailor_update.cgi",
                        radios=dict(name="senior",
                                    entries=("senior", "junior"),
                                    labels=("Senior", "Junior"),
                                    rtype="radio")
                        )

        print_html(form, "Add new sailor", active="SAILORS")

    except Exception as e:
        print_html("", "An error occurred!", "SAILORS")

if __name__ == "__main__":
    add_sailor_form()
