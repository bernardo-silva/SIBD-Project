#!/usr/bin/python3

from utils import get_index_html, set_active_page, print_html
import psycopg2

IST_ID = 'ist193365'
host = 'db.tecnico.ulisboa.pt'
port = 5432
password = 'yczp2585'
db_name = IST_ID


def connect_to_database():
    connect_query = f"host={host} port={port} user={IST_ID} password={password} dbname={db_name}"
    connection = psycopg2.connect(connect_query)

    return connection
    print(connection)


if __name__ == "__main__":
    connect_to_database()
    print_html("")
