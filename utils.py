import json
import sqlite3

DBPATH = 'netflix.db'


def run_query_and_fetch(query, db_path):
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    con.close()
    return result


def search_by_title(title):
    result = []

    query = f"""
                SELECT title, country, release_year, listed_in, description
                FROM netflix
                WHERE title = '{title}'
                ORDER BY main.netflix.release_year DESC
                """

    query_data = run_query_and_fetch(query, DBPATH)
    print(query_data)

    for row in query_data:
        if row:
            result.append({
                    "title": row[0],
                    "country": row[1],
                    "release_year": row[2],
                    "genre": row[3],
                    "description": row[4]
                })
    return result


def search_by_year(year_to, year_after):
    result = []

    query = f"""
                SELECT title, release_year
                FROM netflix
                WHERE release_year BETWEEN '{year_to}' AND '{year_after}'
                LIMIT 100
                """

    query_data = run_query_and_fetch(query, DBPATH)

    for row in query_data:
        if row:
            result.append({
                    "title": row[0],
                    "release_year": row[1],
                })
    return result


def search_by_rating(rating_list):
    result = []

    if len(rating_list) == 1:
        rating_one = rating_list[0]
        query = f"""
                    SELECT title, rating, description
                    FROM netflix
                    WHERE rating = '{rating_one}'
                    """
    elif len(rating_list) == 2:
        rating_one = rating_list[0]
        rating_two = rating_list[1]
        query = f"""
                    SELECT title, rating, description
                    FROM netflix
                    WHERE rating IN ('{rating_one}', '{rating_two}')
                    """
    elif len(rating_list) == 3:
        rating_one = rating_list[0]
        rating_two = rating_list[1]
        rating_three = rating_list[2]
        query = f"""
                    SELECT title, rating, description
                    FROM netflix
                    WHERE rating IN ('{rating_one}', '{rating_two}', '{rating_three}')
                    """

    query_data = run_query_and_fetch(query, DBPATH)

    for row in query_data:
        if row:
            result.append({
                    "title": row[0],
                    "rating": row[1],
                    "description": row[2]
                })
    return result


def search_by_genre(genre):
    result = []

    query = f"""
            SELECT title, description
            FROM netflix
            WHERE listed_in LIKE '%{genre}%'
            ORDER BY release_year DESC 
            LIMIT 10
            """
    query_data = run_query_and_fetch(query, DBPATH)

    for row in query_data:
        if row:
            result.append({
                        "title": row[0],
                        "description": row[1]
                            })

    return result


def search_by_params(show_type, show_release_year, show_genre):
    result = []

    query = f"""
            SELECT title, description
            FROM netflix
            WHERE type = '{show_type}' 
            AND release_year = {show_release_year}
            AND listed_in LIKE '%{show_genre}%'
            """

    query_data = run_query_and_fetch(query, DBPATH)

    for row in query_data:
        if row:
            result.append({
                        "title": row[0],
                        "description": row[1]
                            })
    result = json.dumps(result)

    return result

