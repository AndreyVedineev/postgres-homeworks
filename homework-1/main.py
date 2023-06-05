import csv
import os

import psycopg2

path1 = os.path.join('north_data', 'employees_data.csv')
path2 = os.path.join('north_data', 'customers_data.csv')
path3 = os.path.join('north_data', 'orders_data.csv')

"""Скрипт для заполнения данными таблиц в БД Postgres."""


def main():
    conn = psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password='11122'
    )
    try:
        with open(path1, encoding='UTF-8', newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(csvfile)
            print(headers)
            for row in reader:
                with conn:
                    with conn.cursor() as cur:
                        cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", row)
    finally:
        conn.close()

    try:
        with open(path2, encoding='UTF-8', newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(csvfile)
            print(headers)
            for row in reader:
                with conn:
                    with conn.cursor() as cur:
                        cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", row)
    finally:
        conn.close()

    try:
        with open(path3, encoding='UTF-8', newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(csvfile)
            print(headers)
            for row in reader:
                with conn:
                    with conn.cursor() as cur:
                        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", row)
    finally:
        conn.close()


if __name__ == '__main__':
    main()
