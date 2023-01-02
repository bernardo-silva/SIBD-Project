import psycopg2
from dataclasses import dataclass
import sys
sys.path.insert(0, "~/sibd/project")

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
    with open("/afs/.ist.utl.pt/users/6/5/ist193365/web/sibd/template.html", "r") as f:
        return f.read()


def set_active_page(page):
    pages = dict(HOME="", SAILORS="", RESERVATIONS="", TRIPS="")
    pages[page.upper()] = "active"
    return pages


def print_html(body, header, active):
    html = get_index_html()
    active = set_active_page(active)

    print('Content-type:text/html\n\n')
    print(html.format(BODY=body, HEADER=header, **active))


def get_html_table(contents, header, actions=[]):
    table = '<div class="table-responsive" style="max-width: 98%;margin: 0 auto;">\n\t<tr>\n'
    table += '\n<table class="my-auto table table-striped table-hover">\n\t<tr>\n'

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

            table += f'\t\t<td><a class="btn btn-primary" href="{href}">{action.description}</a></td>\n'

        table += "\t</tr>\n"

    table += "</table>\n</div>\n"

    return table


def get_button(text, href, color="success"):
    button = f'\n\t <a type="button" class="btn btn-{color} m-3 fs-5" href={href}>'
    button += text
    button += '</a>\n'

    return button


def get_form(entries=[], labels=[], types=[], action=[], radios=None, selects=None):
    form = f'\n\t<form action="{action}" method="post">'

    if selects is not None:
        for select in selects:
            form += get_selects(**select)

    for entry, label, ftype in zip(entries, labels, types):
        form += '\n\t\t<div class="mb-3">'
        form += f'\n\t\t\t<label for="{entry}" class="form-label">{label}</label>'
        form += f'\n\t\t\t<input type="{ftype}" class="form-control" name="{entry}" id="{entry}" required>'
        form += '\n\t\t</div>'

    if radios is not None:
        form += get_radios(**radios)


    form += '\n\t<p><input type="submit" class="btn btn-primary" value="Submit"/></p>'
    form += '\n\t</form>'
    return form


def get_radios(name, entries, labels, rtype="checkbox"):
    radios = ""
    for n, (entry, label) in enumerate(zip(entries, labels)):
        radios += '\n\t<div class="form-check form-check-inline">'
        radios += f'\n\t\t<input class="form-check-input" type="{rtype}" '
        radios += f'name={name} id="{entry}" value="{entry}" {"checked" if n==0 else ""}>'
        radios += f'\n\t\t<label class="form-check-label" for="{entry}">{label}</label>'
        radios += '\n\t</div>'
    return radios

def get_selects(name, label, options):
    dropdown = f'\n\t<label for="{name}">{label}</label>'
    dropdown += f'\n\t<select class="mb-3 form-select" name="{name}" id="{name}">'

    options = [list(map(str, o)) for o in options]
    for option in options:
        dropdown += f'\n\t\t<option value="{";".join(option)}">{" ".join(option)}</option>'

    dropdown += '</select>'
    return dropdown
