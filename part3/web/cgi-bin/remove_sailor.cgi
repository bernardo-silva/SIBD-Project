#!/usr/bin/python3

from utils import print_html, get_button
import cgi


def add_sailor_form():
    try:
        email = cgi.FieldStorage().getvalue("email")

        confirmation = f"\n<p> Are you sure you want to remove {email}?</p>"

        button = get_button("Remove",
                            f"/cgi-bin/remove_sailor_update.cgi?email={email}",
                            color="danger")
        
        print_html(confirmation + button, "Remove sailor", active="SAILORS")

    except Exception as e:
        print_html(f"<h1>An error occurred!</h1><p>{e}</p>", "Error",
                   active="SAILORS")


if __name__ == "__main__":
    add_sailor_form()
