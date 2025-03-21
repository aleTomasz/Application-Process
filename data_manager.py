from psycopg import sql

import database_common

@database_common.connection_handler
def get_mentors(cursor):
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        ORDER BY first_name"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_mentors_by_last_name(cursor, last_name):
    query = sql.SQL("""
        SELECT first_name, last_name, city
        FROM mentor
        WHERE last_name ILIKE %(last_name)s
        ORDER BY first_name
        """)
    params = {"last_name": f'%{last_name}%'}
    cursor.execute(query, params)
    return cursor.fetchall()


@database_common.connection_handler
def get_unique_cities(cursor):
    query = sql.SQL("""
    SELECT DISTINCT city from mentor
    """)
    cursor.execute(query)
    return cursor.fetchall()

@database_common.connection_handler
def get_mentors_by_cities(cursor, city_name):
    query = sql.SQL("""
        SELECT first_name, last_name, city
        FROM mentor
        WHERE city ILIKE %(city_name)s
        ORDER BY first_name
        """)
    params = {"city_name": f'{city_name}'}
    cursor.execute(query, params)
    return cursor.fetchall()

@database_common.connection_handler
def get_applicants_data_by_name(cursor, first_name):
    query = sql.SQL("""
        SELECT concat( first_name, ' ', last_name) as full_name, phone_number
        FROM applicant
        WHERE first_name ILIKE %(first_name)s
        ORDER BY first_name
        """)
    params = {"first_name": f'{first_name}'}
    cursor.execute(query, params)
    return cursor.fetchall()