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
    

def print_html(body):
    html = get_index_html()
    active = set_active_page("sailors")

    print('Content-type:text/html\n\n')
    print(html.format(BODY="AAAAAA", **active))

