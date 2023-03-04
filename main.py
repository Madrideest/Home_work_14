from flask import Flask, render_template, request
from utils import search_by_title, search_by_year, search_by_rating, search_by_genre


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/search')
def search():
    s = request.args.get('s')
    film_count = 0
    if s:
        data = search_by_title(s)
        film_count = len(data)
        return render_template('search.html', film_count=film_count, data=data)
    else:
        return render_template('search.html', film_count=film_count)


@app.route('/movie/year/to/year')
def search_by_year_to_year():
    to_year = request.args.get('to')
    after_year = request.args.get('after')
    film_count = 0
    if to_year and after_year:
        data = search_by_year(to_year, after_year)
        film_count = len(data)
        return render_template('year_to_year.html', film_count=film_count, data=data)
    else:
        return render_template('year_to_year.html', film_count=film_count)


@app.route('/rating/children')
def search_by_rating_children():
    data = search_by_rating(['G'])
    film_count = len(data)
    return render_template('rating.html', film_count=film_count, data=data)


@app.route('/rating/family')
def search_by_rating_family():
    data = search_by_rating(['G', 'PG', 'PG-13'])
    film_count = len(data)
    return render_template('rating.html', film_count=film_count, data=data)


@app.route('/rating/adult')
def search_by_rating_adult():
    data = search_by_rating(['R', 'NC-17'])
    film_count = len(data)
    return render_template('rating.html', film_count=film_count, data=data)


@app.route('/genre/<genre>')
def search_by_genre_page(genre):
    data = search_by_genre(genre)
    film_count = len(data)
    return render_template('rating.html', film_count=film_count, data=data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
