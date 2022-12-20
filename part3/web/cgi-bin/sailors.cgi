#!/usr/bin/python3

from utils import print_html, get_html_table, connect_to_database

IST_ID = 'ist193365'
host = 'db.tecnico.ulisboa.pt'
port = 5432
password = 'yczp2585'
db_name = IST_ID


def sailors():
    try:
        connection = connect_to_database(host, port, IST_ID, password, db_name)
        cursor = connection.cursor()

        query = "SELECT * FROM sailor;"
        cursor.execute(query)
        result = cursor.fetchall()

        table = get_html_table(result, ["E-mail", "First Name", "Last Name"])

        print_html(table, "SAILORS")
    except Exception as e:
        print_html(f"<h1>An error occurred!</h1><p>{e}</p>", "SAILORS")
    finally:
        if connection is not None:
            connection.close()
        
        
        


if __name__ == "__main__":
    sailors()
