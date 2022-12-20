import psycopg2

def connect_to_database(host, port, IST_ID, password, db_name):
    credentials = f"host={host} port={port} user={IST_ID} password={password} dbname={db_name}"
    connection = psycopg2.connect(credentials)

    return connection

def get_index_html():
    with open("index.html", "r") as f:
        return f.read()


def get_footer():
    with open("footer.html", "r") as f:
        return f.read()


def set_active_page(page):
    pages = dict(HOME="", SAILORS="", RESERVATIONS="")
    pages[page.upper()] = "active"
    print(pages)
    return pages
    

def print_html(body, header):
    html = get_index_html()
    active = set_active_page("sailors")

    print('Content-type:text/html\n\n')
    print(html.format(BODY=body, HEADER=header, **active))


def get_html_table(contents, header):
    table = '<table class="my-auto table table-striped table-hover">\n\t<tr>\n'

    for col in header:
        table += f'\t\t<th class="table-primary">{col}</th>\n'
    table += "\t</tr>\n"

    for row in contents:
        table += "\t<tr>\n"
        for value in row:
            table += f"\t\t<td>{value}</td>\n"
        table += "\t</tr>\n"

    table += "</table>\n"

    return table
