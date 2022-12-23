#!/usr/bin/python3
import sys
sys.path.insert(0, "/home/bs/Cloud/5_ano/1_semestre/sibd/project/part3")

from utils import print_html, get_button
import cgi


def remove_sailor_form():
    try:
        email = cgi.FieldStorage().getvalue("email")

        confirmation = f"\n<p> Are you sure you want to remove {email}?</p>"

        button = get_button("Remove",
                            f"/cgi-bin/sailor/remove_sailor_update.cgi?email={email}",
                            color="danger")
        
        print_html(confirmation + button, "Remove sailor", active="SAILORS")

    except Exception as e:
        print_html(f"<h1>An error occurred!</h1><p>{e}</p>", "Error",
                   active="SAILORS")


if __name__ == "__main__":
    remove_sailor_form()
