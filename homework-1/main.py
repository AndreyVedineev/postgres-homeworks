"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os

import psycopg2

path1 = os.path.join('north_data', 'employees_data.csv')
path2 = os.path.join('north_data', 'customers_data.csv')
path3 = os.path.join('north_data', 'orders_data.csv')

insert_emp = "INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)"
insert_cust = "INSERT INTO customers VALUES (%s, %s, %s)"
insert_order = "INSERT INTO orders VALUES (%s, %s, %s, %s, %s)"


def insert_tabl(path, insert):
    conn = psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password='11122'
    )
    try:
        with open(path, encoding='UTF-8', newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(csvfile)
            print(headers)
            for row in reader:
                with conn:
                    with conn.cursor() as cur:
                        cur.execute(insert, row)
    finally:
        conn.close()


if __name__ == '__main__':
    insert_tabl(path1, insert_emp)
    insert_tabl(path2, insert_cust)
    insert_tabl(path3, insert_order)
