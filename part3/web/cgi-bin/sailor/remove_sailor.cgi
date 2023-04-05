#!/usr/bin/python3
import cgi
import sys
sys.path.insert(0, "/afs/.ist.utl.pt/users/6/5/ist193365/web/sibd")

from utils import print_html, get_button


def remove_sailor_form():
    try:
        email = cgi.FieldStorage().getvalue("email")

        confirmation = f"\n<p> Are you sure you want to remove {email}?</p>"

        confirm_button = get_button("Remove",
                                    f"remove_sailor_update.cgi?email={email}",
                                    color="danger")
        cancel_button = get_button("Cancel", "sailor.cgi", color="secondary")

        body = '<div class="text-center">\n' + confirmation + confirm_button + cancel_button + '</div>'
        print_html(body, "Remove sailor", active="SAILORS")

    except Exception as e:
        print_html("", "An error occurred!", "SAILORS")


if __name__ == "__main__":
    remove_sailor_form()
