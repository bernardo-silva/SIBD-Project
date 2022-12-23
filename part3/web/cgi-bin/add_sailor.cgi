#!/usr/bin/python3

from utils import print_html, get_form


def add_sailor_form():
    try:
        form = get_form(entries=["email", "firstname", "surname"],
                        labels=["E-mail:", "First name:", "Surname:"],
                        types=["email", "text", "text"])

        print_html(form, "Add new sailor", active="SAILORS")

    except Exception as e:
        print_html(f"<h1>An error occurred!</h1><p>{e}</p>", "Error",
                   active="SAILORS")


if __name__ == "__main__":
    add_sailor_form()
