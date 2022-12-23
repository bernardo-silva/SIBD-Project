import psycopg2
from dataclasses import dataclass


@dataclass
class Action():
    description: str
    script: str
    parameters: list
    columns: list

    @property
    def query(self):
        return r"={}&".join(self.parameters) + "={}"


def connect_to_database(host, port, IST_ID, password, db_name):
    credentials = f"host={host} port={port} user={IST_ID} password={password} dbname={db_name}"
    connection = psycopg2.connect(credentials)

    return connection


def get_index_html():
    with open("index.html", "r") as f:
        return f.read()


def set_active_page(page):
    pages = dict(HOME="", SAILORS="", RESERVATIONS="")
    pages[page.upper()] = "active"
    print(pages)
    return pages


def print_html(body, header, active):
    html = get_index_html()
    active = set_active_page(active)

    print('Content-type:text/html\n\n')
    print(html.format(BODY=body, HEADER=header, **active))


def get_html_table(contents, header, actions=[]):
    table = '<table class="my-auto table table-striped table-hover">\n\t<tr>\n'

    for col in header:
        table += f'\t\t<th class="table-primary">{col}</th>\n'
    table += "\t</tr>\n"

    for row in contents:
        table += "\t<tr>\n"
        for value in row:
            table += f"\t\t<td>{value}</td>\n"

        for action in actions:
            href = action.script + "?" + \
                action.query.format(*[row[i] for i in action.columns])

            table += f'\t\t<td><a href="{href}">{action.description}</a></td>\n'

        table += "\t</tr>\n"

    table += "</table>\n"

    return table


def get_button(text, href, color="primary"):
    button = f'\n\t <a type="button" class="btn btn-{color}" href={href}>'
    button += text
    button += '</a>\n'

    return button


def get_form(entries, labels, types):
    form = '\n\t<form action="add_sailor_update.cgi" method="post">'
    for entry, label, ftype in zip(entries, labels, types):
        form += '\n\t\t<div class="mb-3">'
        form += f'\n\t\t\t<label for="{entry}" class="form-label">{label}</label>'
        form += f'\n\t\t\t<input type="{ftype}" class="form-control" name="{entry}" id="{entry}">'
        form += '\n\t\t</div>'

    form += '\n\t<p><input type="submit" class="btn btn-primary" value="Submit"/></p>'
    form += '\n\t</form>'
    return form
